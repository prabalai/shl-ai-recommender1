from fastapi import APIRouter
from models.request_models import ChatRequest
from services.conversation_service import process_chat

router = APIRouter()

@router.post("/chat")
def chat(req: ChatRequest):
    return process_chat(req.messages)