# Задача 2. Напишите программу, которая позволяет считывать из файла вопрос, отвечать на него и отправлять ответ обратно пользователю.

import telebot
from telebot import types
import requests
import time

bot = telebot.TeleBot("6197213883:AAGZe0-JIGR2qN36BLboFR9WlIkpOYvi6Sk", parse_mode=None)