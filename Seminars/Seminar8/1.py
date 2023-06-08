# Задача 1 : Напишите чат-бота, который записывает сообщения всех пользователей, которые ему написали.
import telebot
from telebot import types
import requests
import time

bot = telebot.TeleBot("6197213883:AAGZe0-JIGR2qN36BLboFR9WlIkpOYvi6Sk", parse_mode=None)

markup = types.ReplyKeyboardMarkup(row_width=1)
btn_reg = types.KeyboardButton('регистрация')
btn_alarm = types.KeyboardButton('оповещение')
markup.add(btn_reg,btn_alarm)





@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.from_user.id, "Привет, я твой бот ", reply_markup=markup)
	
@bot.message_handler(content_types=['text'])
def text_message(message):
	# print(message)
	data = open("log.txt",mode='a', encoding='utf-8')
	text = f'{message.from_user.first_name} {message.from_user.last_name}: {message.text}\n'  # в каком виде мы хотим получить текст
	data.write(text)
	data.close()
	

	if message.text == "регистрация":
		data = open("registred_useres.txt", mode='r', encoding='utf-8')
		id_list = data.readlines()
		data.close()
		id_list = list(el[:-1] for el in id_list)
		if str(message.from_user.id) not in id_list:
			data = open("registred_useres.txt",mode='a', encoding='utf-8')
			data.write(f"{message.from_user.id}\n")
			data.close()
			bot.reply_to(message,"Регистрация прошла успешно!")
		else:
			bot.reply_to(message, "Вы уже зарегистрованны")
	elif message.text == "оповещение":
		data = open("registred_useres.txt", mode='r', encoding='utf-8')
		id_list = data.read().split("\n")
		data.close()
		for id in id_list:
			bot.send_message(id, "Совещание через 5 минут")

        
    


	






bot.polling() # Должен оставаться в самом конце