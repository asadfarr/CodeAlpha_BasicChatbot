import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

# Define patterns and responses for the chatbot
pairs = [
    ("hi|hello|hey|hii", ["Hello!", "Hlw", "Hi there!", "Hey!"]),
    ("ok sorry|sorry",["No problem","It's okay"]),
    ("how are you?", ["I'm good,What about you?" , "superb, you?", "I'm doing well, how are you?."]),
    ("your name?|who are you?", ["I am a chatbot.", "You can call me Chatbot."]),
    ("i am good|fine|i am also good|i am fine",["good to hear"]),
("who made you|who built you|who developed you|who is your owner",["My owner is Asad Khan","Asad Khan"]),
    ("what is your purpose?", ["I'm here to assist you and have conversations."]),
    ("by|bye|goodbye|ok by", ["Goodbye!", "See you later.", "Bye!"]),
    ("what is your age",["Never ask age of chatbot hehehe but yeah i am still young"])
    # You can add more patterns and responses here
]

# Create a Chat object
chatbot = Chat(pairs, reflections)

# Start chatting
print("Hello! I'm a simple chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)