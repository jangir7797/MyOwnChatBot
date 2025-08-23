import os
import requests
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # Load environment variables from .env

API_KEY = os.getenv("GOOGLE_AI_API_KEY")

def ask_google_ai(user_prompt):
    # # import pdb; pdb.set_trace()
    # url = f"https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText?key={API_KEY}"

    # headers = {
    #     "Content-Type": "application/json"
    # }

    # data = {
    #     "prompt": {
    #         "text": "Explain AI simply"
    #     },
    #     "temperature": 0.7,
    #     "maxTokens": 150
    # }

    # response = requests.post(url, headers=headers, json=data)

    # if response.status_code == 200:
    #     return response.json()['candidates'][0]['output']
    # else:
    #     raise Exception(f"API Error {response.status_code}: {response.text}")
    
    # Configure the API key (replace with your own key)
    genai.configure(api_key=API_KEY)

    # Create an instance of the Gemini model (choose available model, e.g. gemini-1.5-flash)
    model = genai.GenerativeModel("gemini-2.0-flash")

    # Generate a response
    response = model.generate_content(user_prompt)
    if response:
        return response
    else:
        raise Exception("API Error: No response from Google AI")
    
