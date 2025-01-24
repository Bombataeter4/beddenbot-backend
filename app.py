
from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2"
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")  # Token uit environment variables

headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

def query_huggingface(payload):
    response = requests.post(HUGGINGFACE_API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    payload = {
        "inputs": f"As an expert in beds: {user_input}",
        "parameters": {"max_new_tokens": 50, "temperature": 0.8},
    }
    try:
        result = query_huggingface(payload)
        return jsonify({"response": result[0]["generated_text"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
