import os
import requests
import openai
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

API_URL_PERPLEXITY = "https://api.perplexity.ai/chat/completions"

# Perplexity

def chat_perplexity(prompt):
    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "pplx-70b-chat",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    try:
        response = requests.post(API_URL_PERPLEXITY, headers=headers, json=data, timeout=10)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"].strip()
        else:
            return None, f"Perplexity Error: {response.status_code} - {response.text}"
    except Exception as e:
        return None, f"Perplexity Exception: {e}"

# OpenAI

def chat_openai(prompt):
    try:
        openai.api_key = OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            timeout=10
        )
        return response.choices[0].message["content"].strip(), None
    except Exception as e:
        return None, f"OpenAI Exception: {e}"

# Gemini

def chat_gemini(prompt):
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text.strip(), None
    except Exception as e:
        return None, f"Gemini Exception: {e}"

# Try all providers

def chat_bot(prompt):
    # Try OpenAI
    result, error = chat_openai(prompt)
    if result:
        return result
    # Try Perplexity
    result, error = chat_perplexity(prompt)
    if result:
        return result
    # Try Gemini
    result, error = chat_gemini(prompt)
    if result:
        return result
    # If all fail, return last error
    return error or "All providers failed."

if __name__ == "__main__":
    while True:
        prompt = input("User: ")
        if prompt.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_bot(prompt)
        print("Chatbot:", response)