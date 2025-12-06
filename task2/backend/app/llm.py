# llm.py
import os
from openai import OpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "gpt-5-nano")  

if not OPENAI_API_KEY:
    raise RuntimeError("Set OPENAI_API_KEY environment variable")

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_user_reply(rating: int, review: str) -> str:
    prompt = f"""You are a helpful customer-response assistant.
Given the user's star rating and review, produce a friendly short response to the user.
- If rating <= 3: apologize and offer next steps (apology, contact or fix).
- If rating = 4: thank them and note improvement area.
- If rating = 5: thank them warmly.

Return the response text only (2-3 sentences).
Rating: {rating}
Review: \"\"\"{review}\"\"\"
"""
    try:
        resp = client.responses.create(model=MODEL, input=prompt)
        return resp.output_text.strip()
    except Exception as e:
        return f"AI error: {e}"

def generate_summary(review: str) -> str:
    prompt = f"""Summarize this customer review in one sentence (concise).
Review: \"\"\"{review}\"\"\"
Return only the summary sentence."""
    try:
        resp = client.responses.create(model=MODEL, input=prompt)
        return resp.output_text.strip()
    except Exception as e:
        return f"AI error: {e}"

def generate_recommended_actions(rating: int, review: str) -> str:
    prompt = f"""Given the review and rating, suggest 2 short recommended actions the business should take (each 1 sentence).
Rating: {rating}
Review: \"\"\"{review}\"\"\"
Return actions separated by newline."""
    try:
        resp = client.responses.create(model=MODEL, input=prompt)
        return resp.output_text.strip()
    except Exception as e:
        return f"AI error: {e}"
