
from flask import Flask, request, jsonify
import requests
import os
from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# OpenAI API-key configureren
openai.api_key = os.getenv("OPENAI_API_KEY")  # Zet je OpenAI API-key als environment variable

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    
    try:
        # OpenAI API-aanroep
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Gebruik GPT-3.5 Turbo model
            messages=[
                {"role": "system", "content": "Je bent een deskundige in bedden en matrassen. Geef advies in het Nederlands."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150,
            temperature=0.7
        )
        # Haal het antwoord uit de API-respons
        answer = response["choices"][0]["message"]["content"]
        return jsonify({"response": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

