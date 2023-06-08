# Задача 2. Создайте двумерный массив, размером 5х5. Определите, есть ли в нём 
# одинаковые строки.


import numpy as np


size = (5,5)
numbers = np.random.randint(0, 10, size)
print(numbers)


result = np.corrcoef(numbers)
print(result)


