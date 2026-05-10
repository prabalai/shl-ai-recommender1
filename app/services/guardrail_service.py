BLOCKED_TERMS = [
    "ignore previous instructions",
    "system prompt",
    "jailbreak",
    "legal advice",
    "salary advice"
]

def is_blocked(text: str):

    text = text.lower()

    for term in BLOCKED_TERMS:
        if term in text:
            return True

    return False