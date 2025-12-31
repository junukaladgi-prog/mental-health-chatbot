import datetime
import os

# Function to detect mood
def detect_mood(user_input):
    mood_keywords = {
        "sad": "It's okay to feel sad sometimes. You're not alone 💙",
        "happy": "That's wonderful to hear! 😊",
        "stressed": "Try taking deep breaths or a short walk. You've got this 🌿",
        "anxious": "Anxiety can be tough. Remember, this moment will pass 🤝",
        "angry": "Anger is valid. Let’s take a deep breath together 🔥",
        "lonely": "You're not alone. I'm always here to chat 🫂",
        "down": "Sending you a big virtual hug 🤗",
        "depressed": "That must be really hard. You're not alone, and help is available 🌧️💛",
        "tired": "Rest is important. Don’t forget to take care of yourself 😴",
        "hopeless": "Even the darkest nights end with sunrise. You're stronger than you think ☀️",
        "help": "You're doing great for reaching out. Would you like some resources or emergency support? ❤️",
        "support": "You're so brave to speak up. I'm here to support you 💌"
    }

    for keyword, response in mood_keywords.items():
        if keyword in user_input.lower():
            return keyword, response
    return None, None

# Log mood with timestamp
def log_mood(mood):
    with open("mood_log.txt", "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - Mood: {mood}\n")

# Emergency support function
def emergency_support():
    return (
        "\n🚨 It sounds like you're going through a tough time.\n"
        "Here are a few things you can do right now:\n"
        "📞 Talk to a friend or family member you trust.\n"
        "🆘 If it's an emergency, please reach out to a local helpline.\n"
        "🌐 You can also visit: https://findahelpline.com for global mental health support.\n"
    )

# Chatbot intro
print("👋 Hello! I'm your Mental Health Chatbot.")
print("You can talk to me about how you're feeling.")
print("Type 'bye' to end the chat.\n")

# Chat loop
while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Bot: Take care of yourself. I'm always here if you need to talk 💙")
        break

    if "urgent help" in user_input.lower() or "emergency" in user_input.lower():
        print(emergency_support())
        continue

    mood, response = detect_mood(user_input)

    if mood:
        print("Bot:", response)
        log_mood(mood)
    else:
        print("Bot: I'm not sure I understood that, but I'm here for you 🫶")
