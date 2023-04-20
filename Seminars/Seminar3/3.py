import random

# Задача 3. Напишите скрипт генератора паролей заданной длины, состоящих из латинских букв и чисел.


length = int(input("Введите длину пароля: "))
symbols = "qwertyuiopasdfghjklzxcvbnm0123456789"
password =[symbols[random.randint(0,len(symbols))] for el in range(length)]
print(password)