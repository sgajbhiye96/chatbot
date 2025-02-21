from flask import Flask, render_template, request, jsonify
from transformers import pipeline, set_seed

app = Flask(__name__)

# Initialize text generation pipeline
chatbot = pipeline("text-generation", model="gpt2")
set_seed(42)

# Store conversation history
conversation_history = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_id = request.remote_addr
    user_input = request.json["message"]

    # Retrieve or initialize user conversation history
    history = conversation_history.get(user_id, "")
    prompt = history + f"\nUser: {user_input}\nBot:"

    # Generate bot response
    response = chatbot(prompt, max_length=100, do_sample=True, temperature=0.7)[0]['generated_text']

    # Extract only the bot's reply
    bot_reply = response.split("Bot:")[-1].strip().split("User:")[0].strip()

    # Update history
    conversation_history[user_id] = prompt + f" {bot_reply}\n"

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
