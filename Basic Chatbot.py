import spacy
import random

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")

# Predefined responses and patterns
responses = {
    "greeting": ["Hello! How can I help you today?", "Hi there! How's it going?", "Hello! What can I do for you?"],
    "farewell": ["Goodbye! Have a great day!", "Bye! Take care!", "See you soon!"],
    "how_are_you": ["I'm doing great, thank you for asking!", "I'm fine, how about you?", "I'm good, thanks!"],
    "name": ["I am a chatbot. You can call me Chatbot!", "I don't have a specific name, but I am Chatbot."],
    "joke": ["Why don't skeletons fight each other? They don't have the guts!", "Why did the math book look sad? Because it had too many problems!"],
    "default": ["Sorry, I didn't understand that. Could you rephrase?", "I'm not sure what you mean. Can you try again?"]
}

# Function to handle user input and generate a response
def get_response(user_input):
    # Process the input with spaCy
    doc = nlp(user_input.lower())

    # Identify common intents (patterns) from user input
    if any(token in ["hi", "hello", "hey", "hola"] for token in doc):
        return random.choice(responses["greeting"])
    
    elif any(token in ["bye", "goodbye", "exit"] for token in doc):
        return random.choice(responses["farewell"])

    elif any(token in ["how", "are", "you"] for token in doc):
        return random.choice(responses["how_are_you"])

    elif "name" in user_input.lower():
        return random.choice(responses["name"])

    elif "joke" in user_input.lower():
        return random.choice(responses["joke"])

    # Default response if no pattern is matched
    return random.choice(responses["default"])

# Main function to initiate the chatbot
def chatbot():
    print("Hi, I'm Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot
if __name__ == "__main__":
    chatbot()