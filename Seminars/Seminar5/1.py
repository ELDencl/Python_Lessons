import random

# Задача 1. На вход подаётся четырёхзначное число.
# Получите список, состоящий из цифр данного числа, увеличенных на 10.


num = input("Введите число : ")
numbers = [int(letter) for letter in num ]
print(numbers)
numbers = list(map(lambda x : x + 10, numbers))
print(numbers)



# number = input("Введите четырехзначное число: ")
# if len(number) != 4:
#     print("Вы ввели неправильное число")
# else:
#     digits = list(
#     map(
#     lambda x: int(x) + 10, number))
# print(digits)