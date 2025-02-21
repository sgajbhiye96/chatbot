from transformers import pipeline, GenerationConfig

# Use the text-generation pipeline instead of conversational
chatbot = pipeline("text-generation", model="facebook/blenderbot-400M-distill")

# Maintain conversation history
# conversation = Conversation()  # Remove this line

print("🤖 Chatbot: Hi there! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "goodbye", "see you later"]:
        print("🤖 Chatbot: Goodbye! Take care! 👋")
        break

    # conversation.add_user_input(user_input)  # Remove this line
    # Pass the conversation object to the pipeline
    # Instead of passing conversation, pass user_input directly
    response = chatbot(user_input, max_new_tokens=100)  # Adjust max_new_tokens as needed
    
    # GenerationConfig is not needed for Blenderbot
    # response = chatbot(user_input, generation_config=GenerationConfig(max_new_tokens=100))
    
    print("🤖 Chatbot:", response[0]['generated_text']) # Access the generated text from the response