# chatbot.py - Simple rule-based customer service chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "price" in user_input:
        return "Our prices vary depending on the product. Could you specify which one?"
    elif "refund" in user_input:
        return "You can request a refund within 7 days of purchase."
    elif "help" in user_input:
        return "Sure! I'm here to help. Please tell me your query."
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase?"

print("Chatbot: Hello! I'm your customer service assistant.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye! Have a great day.")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
