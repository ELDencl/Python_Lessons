# Задача 1. Дан список элементов. Используя библиотеку NumPy, подсчитайте количество 
# уникальных элементов в нём.


import numpy as np


size = 10
numbers = np.random.randint(0, 10, size)
print(numbers)
uniq_list, uniq_counts = np.unique(numbers, return_counts=True)
print(f"Уникальные элементы : {uniq_list}")
print(f"Их колличество      : {uniq_counts}")
