# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.
# 1 –> Понедельник
# 10 –> Нет такого дня
# 7 –> Воскресение

number = int(input("Введите число соответствующее дню недели : "))

if number == 1:
    print("Поедельник")
if number == 2:
    print("Вторник")
if number == 3:
    print("Среда")
if number == 4:
    print("Четверг")
if number == 5:
    print("Пятница")
if number == 6:
    print("Суббота")
if number == 7:
    print("Воскресенье")
if number < 0 or number > 7 :
    print("нет такого дня ")