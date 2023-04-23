import random

# Создайте кортеж. Запишите в него 10 случайных чисел


numbers = [random.randint(0,10) for _ in range(10)]
numbers = tuple(numbers)

numbers = tuple(random.randint(0,10) for _ in range(10))

print(numbers)
print(type(numbers))