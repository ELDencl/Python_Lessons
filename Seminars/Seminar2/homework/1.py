# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def factorial():
    num = int(input("Введите число : "))
    numbers = []
    for i in range(1,num +1):
        factor = 1
        for j in range(1,i+1):
            factor *= j
        numbers.append(factor)
    print(numbers)

factorial()