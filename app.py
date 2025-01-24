
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

# OpenAI API-key configureren
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get("message", "")
        print(f"Ontvangen bericht: {user_input}")  # Log het bericht

        # OpenAI API-aanroep
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Je bent een deskundige in bedden en matrassen. Geef advies in het Nederlands."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150,
            temperature=0.7
        )
        answer = response["choices"][0]["message"]["content"]
        print(f"Gegenereerd antwoord: {answer}")  # Log het antwoord
        return jsonify({"response": answer})

    except Exception as e:
        print(f"Fout opgetreden: {str(e)}")  # Log de foutmelding
        return jsonify({"error": "Er is een fout opgetreden. Controleer de logs."}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


