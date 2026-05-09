responses = {
    "hi": "Hello 👋",
    "hello": "Hi there!",
    "how are you": "I am fine 😊",
    "what is your name": "I am an AI chatbot created using Python.",
    "who created you": "I was created by a student for a CodSoft internship.",
    "tell me a joke": "Why did the computer sleep? Because it was tired 😄",
    "what can you do": "I can chat with you and answer simple questions.",
    "bye": "Goodbye! Have a nice day 😊"
}

print("=== AI CHATBOT ===")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    found = False

    for question in responses:
        if question in user:
            print("Bot:", responses[question])
            found = True

            if question == "bye":
                exit()

    if not found:
        print("Bot: Sorry, I don't understand that.")