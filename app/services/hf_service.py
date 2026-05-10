import requests
from config import (
    HF_API_TOKEN,
    HF_MODEL
)

API_URL = (
    f"https://api-inference.huggingface.co/models/"
    f"{HF_MODEL}"
)

headers = {
    "Authorization":
    f"Bearer {HF_API_TOKEN}"
}

def query_hf(prompt):

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.2
        }
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json=payload
    )

    return response.json()