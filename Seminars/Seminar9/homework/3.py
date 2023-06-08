# Задача 3. Создайте двумерный массив случайного размера. Найдите индексы 
# максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива



import numpy as np


size = (np.random.randint(5, 10),np.random.randint(5, 10,))
numbers = np.random.randint(0, 10, size)

max_number = np.max(numbers)
ind_max = np.unravel_index(np.argmax(numbers), numbers.shape)
ind_min = np.unravel_index(np.argmin(numbers), numbers.shape)





print(numbers)
diogonal = np.diagonal(numbers)
print(f"Главная диагональ :{diogonal}")
print(f"Индекс максимального значения :{ind_max}")
print(f" Индекс минимального значения :{ind_min}")