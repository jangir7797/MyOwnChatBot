import os
import requests
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # Load environment variables from .env

API_KEY = os.getenv("GOOGLE_AI_API_KEY")

def ask_google_ai(user_prompt):
  genai.configure(api_key=API_KEY)

    # Create an instance of the Gemini model (choose available model, e.g. gemini-1.5-flash)
    model = genai.GenerativeModel("gemini-2.0-flash")

    # Generate a response
    response = model.generate_content(user_prompt)
    if response:
        return response
    else:
        raise Exception("API Error: No response from Google AI")
    
