from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from app.search import search_assessments


from app.services.ranking_service import (
    rerank_results
)

from app.services.guardrail_service import (
    is_blocked
)

app = FastAPI()

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

@app.get("/")
def home():

    return {
        "message": "SHL API Running"
    }

@app.get("/health")
def health():

    return {
        "status": "ok"
    }

@app.post("/chat")
def chat(req: ChatRequest):

    full_conversation = " ".join(
        [m.content for m in req.messages]
    ).lower()

    if is_blocked(full_conversation):

        return {
            "reply":
            "I can only help with SHL assessments.",

            "recommendations": [],

            "end_of_conversation": True
        }

    role_keywords = [
        "developer",
        "engineer",
        "manager",
        "analyst",
        "scientist"
    ]

    has_role = any(
        role in full_conversation
        for role in role_keywords
    )

    if not has_role:

        return {
            "reply":
            (
                "Please specify the role, "
                "seniority level, and whether "
                "you need technical or "
                "personality assessments."
            ),

            "recommendations": [],

            "end_of_conversation": False
        }

    results = search_assessments(
        full_conversation,
        n_results=20
    )

    results = rerank_results(
        results,
        full_conversation
    )

    recommendations = []

    for item in results[:10]:

        recommendations.append({
            "name": item["name"],
            "url": item["url"],
            "test_type": item["keys"]
        })

    return {
        "reply":
        "Here are recommended SHL assessments.",

        "recommendations":
        recommendations,

        "end_of_conversation":
        False
    }
