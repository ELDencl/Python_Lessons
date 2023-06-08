# Задача 3. Задайте квадратную матрицу, состоящую из случайных чисел. Найдите самый часто встречающийся элемент в этой матрице

import numpy as np


size = (4, 4)
numbers = np.random.randint(0, 10, size)
print(numbers)

uniq_list, uniq_counts = np.unique(numbers, return_counts=True)
print(f"Уникальные элементы : {uniq_list}")
print(f"Их колличество      : {uniq_counts}")

index_max = np.argmax(uniq_counts)
print(f"Самый часто встречающийся элемент : {uniq_list[index_max]}")


