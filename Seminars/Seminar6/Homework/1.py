# Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN
# N может быть любой длины.
# N = 132: 132 + 132132 + 132132132 = 132264396




def NNN():
    numbers = input("Введите число: ")
    result = int(numbers) + int(numbers *2) + int(numbers*3)
    print(result)


NNN()