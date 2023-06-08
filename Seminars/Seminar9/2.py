# Задача 2. Дан массив случайных чисел. Создайте его с помощью Numpy. Определите его среднее арефметическое.
# На ввод подается число. Определите ближайшие по значению к нему элемент массива 

# [1.2, 4.2, 5.6, 7.1] -> 4.525
# 6.1 -> 5.6

import numpy as np

size = 10 
numbers = np.random.randint(10,100,size)
print(numbers)

mean = sum(numbers)/len(numbers)
print(f'Среднее арифметическое : {mean}')   # Стандартная python

mean = np.mean(numbers)
print(f'Среднее арифметическое : {mean}')   # Библиотека Numpy



num = int(input("Введите число : "))
dist = [np.abs(el - num) for el in numbers]
print(f'Дистанция{dist}')
min_dist = np.min(dist)
print(f'Минимальное расстояние {min_dist}')
index_min_dist = dist.index(min_dist)
print(f'Индекс минимального расстояния {index_min_dist}')
print(f"{num} -> {numbers[index_min_dist]}")
