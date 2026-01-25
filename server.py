from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__)

GROQ_API_KEY = "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"

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json

    res = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.1-8b-instant",
            "messages": data["messages"],
            "temperature": data.get("temperature", 0.5),
            "max_tokens": data.get("max_tokens", 300)
        }
    )

    return jsonify(res.json()), res.status_code



    return jsonify(res.json()), res.status_code

if __name__ == "__main__":
    app.run(debug=True)