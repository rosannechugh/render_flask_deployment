import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS

# Configure Generative AI
genai.configure(api_key="AIzaSyCfOvUOrHl-y_frEUDII4SF3CNgNTu5jTQ")
model = genai.GenerativeModel()

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow requests from Wix

# Store chat history
chat_history = []

@app.route("/chat", methods=["POST"])
def chatbot():
    global chat_history
    data = request.json
    user_message = data.get("message", "")

    chat_session = model.start_chat(history=chat_history)
    response = chat_session.send_message(user_message)
    model_response = response.text

    # Save chat history
    chat_history.append({"role": "user", "parts": user_message})
    chat_history.append({"role": "model", "parts": model_response})

    return jsonify({"response": model_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
