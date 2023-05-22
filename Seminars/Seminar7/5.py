# Задача 5: Создайте Telegram-бота, добавьте в него метод приветсвия пользователя

import telebot
import requests

bot = telebot.TeleBot("6197213883:AAGZe0-JIGR2qN36BLboFR9WlIkpOYvi6Sk", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")




# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)


@bot.message_handler(content_types=['text'])
def greetings(message):
	# print(message)
	text = message.text
	if "привет" in text:
		bot.reply_to(message, f"Привет! {message.from_user.first_name}")
	elif text == 'погода':
		req = requests.get("https://wttr.in/?0T")
		bot.reply_to(message,req.text)
	elif text == "котики":
		req = requests.get("https://cataas.com/#/cat")
		bot.send_photo(message.chat.id, req.content)
	
	









bot.polling() # Должен оставаться в самом конце