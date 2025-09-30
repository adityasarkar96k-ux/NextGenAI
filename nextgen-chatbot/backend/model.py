import random

def generate_response(user_input):
    user_input = user_input.lower()

    # Simple rules
    if "hello" in user_input or "hi" in user_input:
        return random.choice(["Hello! 👋", "Hi there! How can I help you?", "Hey, welcome to NextGen!"])
    elif "your name" in user_input:
        return "I am **NextGen AI Chatbot** 🤖"
    elif "college" in user_input:
        return "This project is made for college presentation 🎓"
    elif "bye" in user_input:
        return "Goodbye! Have a great day! 🌟"

    # Default fallback
    return random.choice([
        "Interesting... tell me more 🤔",
        "Hmm, I need to think about that...",
        "I’m still learning, but I’ll get better!"
    ])
