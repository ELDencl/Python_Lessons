from random import randint


# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8


spisok = [randint(1, 10) for _ in range(10)]

d = filter(lambda x: x > 5, spisok)
d = list(d)
print(spisok)
print(d)