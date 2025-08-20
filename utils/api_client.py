import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

API_KEY = os.getenv("GOOGLE_AI_API_KEY")

def ask_google_ai(prompt):
    url = "https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "prompt": {
            "text": prompt
        },
        "temperature": 0.7,
        "maxTokens": 150
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['candidates'][0]['output']
    else:
        raise Exception(f"API Error {response.status_code}: {response.text}")
