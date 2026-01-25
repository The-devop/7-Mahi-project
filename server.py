import json
import requests
import os

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

def handler(request):
    if request.method != "POST":
        return {
            "statusCode": 405,
            "body": "Method Not Allowed"
        }

    body = json.loads(request.body)

    res = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.1-8b-instant",
            "messages": body["messages"],
            "temperature": body.get("temperature", 0.5),
            "max_tokens": body.get("max_tokens", 300)
        }
    )

    return {
        "statusCode": res.status_code,
        "headers": { "Content-Type": "application/json" },
        "body": json.dumps(res.json())
    }
