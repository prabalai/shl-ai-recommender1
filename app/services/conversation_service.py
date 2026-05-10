from services.guardrail_service import (
    is_blocked
)

from services.recommendation_service import (
    get_recommendations
)

def process_chat(messages):

    latest_message = messages[-1].content

    if is_blocked(latest_message):

        return {
            "reply":
            "I can only help with SHL assessments.",

            "recommendations": [],

            "end_of_conversation": True
        }

    full_conversation = " ".join(
        [m.content for m in messages]
    ).lower()

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
                "seniority level and whether "
                "you need technical, "
                "personality or simulation "
                "assessments."
            ),

            "recommendations": [],

            "end_of_conversation": False
        }

    recommendations = get_recommendations(
        full_conversation
    )

    return {
        "reply":
        "Here are the best SHL assessments.",

        "recommendations":
        recommendations,

        "end_of_conversation":
        False
    }