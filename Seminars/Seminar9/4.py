#  Задача 4. Дан двумерный массив, заполненый 0 и 1. Определите, есть ли в нем нулевые столбцы.


import numpy as np


size = (3, 6)
numbers = np.random.randint(0, 2, size)
print(numbers)


# result = np.any(numbers > 5)

result = numbers.any(axis=0)
print(result)
result = ~result
print(result)


if True in result:
    print("В матрице есть столбец, состоящий из нулей")
else:
    print("В матрице нету столбца, состоящий из нулей")
