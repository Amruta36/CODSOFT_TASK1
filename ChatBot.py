import random

# Define the rules and corresponding responses
rules = {
    "hey": ["Hello!", "Hi there!", "Hey!"],
    "what's your name": ["I'm just a simple chatbot.", "I don't have a name, but you can call me Chatbot.",
                         "I'm your friendly neighborhood chatbot!"],
    "what is AI?":["I'm not sure I understand."],
    "what is web development":["The word Web Development is made up of two words, that is: Web: It refers to websites, "
                               "web pages or anything that works over the internet."
                               " Development: It refers to building the application from scratch"],
    "what is ML": ["Machine learning (ML) is a branch of artificial intelligence (AI) and computer science that focuses on the using data "
                  "and algorithms to enable AI "
                  "to imitate the way that humans learn, gradually improving its accuracy."],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "default": ["I'm not sure I understand.", "Could you please rephrase that?",
                "I'm still learning. Can you ask me something else?"]
}


# Function to generate response based on user input
def generate_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check if user input matches any rule
    for pattern, responses in rules.items():
        if pattern in user_input:
            return random.choice(responses)

    # If no specific rule matches, return a default response
    return random.choice(rules["default"])


# Main function to handle user interaction
def chat():
    print("Welcome to the Rule-Based Chatbot!")
    print("You can start chatting. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: " + generate_response(user_input))
            break
        else:
            print("Chatbot: " + generate_response(user_input))


# Run the chatbot
if __name__ == "__main__":
    chat()
