import telebot
import os


bot = telebot.TeleBot(os.environ["TOKEN"], parse_mode=None)

# Replace 'YOUR_BOT_TOKEN' with the actual token you obtained from BotFather

user_id = 960867942

document_path = 'google_maps_data.csv'

with open(document_path, 'rb') as document:
    bot.send_document(user_id, document)