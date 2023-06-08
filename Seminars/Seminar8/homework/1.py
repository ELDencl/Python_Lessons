# Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.




import telebot
from telebot import types
import requests
import time

bot = telebot.TeleBot("6197213883:AAGZe0-JIGR2qN36BLboFR9WlIkpOYvi6Sk", parse_mode=None)


@bot.message_handler(content_types=['text'])
def save_message(message):
    data = open("user_message.txt", mode="a", encoding="utf-8")
    text = f'{message.from_user.first_name} {message.from_user.last_name}: {message.text}\n'
    data.write(text)
    data.close()


bot.polling()