from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create chatbot
bot = ChatBot("test")

# Create trainer
trainer = ListTrainer(bot)

# Load conversation file
with open('NLP/conversations.txt', 'r') as file:
    conv = file.readlines()

# Train the bot
trainer.train(conv)

# Chat loop
while True:
    message = input("you: ")

    if message.lower() == "bye":
        print("bot: Goodbye!")
        break

    response = bot.get_response(message)
    print("bot:", response)