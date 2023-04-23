import random




# Сгенерируйте список случайных чисел от 1 до 20, состоящий из 10 элементов.
# Удалите из списка дубликаты уже имеющихся элементов. Определите, сколько элементов было удалено.

numbers = [random.randint(0,20) for _ in range(10)]



# def unic(numbers):
#     i = 0
#     count = 0
#     for el in numbers:
#         while i < len(numbers)-1:
#             if numbers[i+1] == el:
#                 count += 1
#                 numbers.pop(i+1)
#             i += 1
#     return numbers



# print(numbers)
# print(unic(numbers))



numbers_new = set(numbers)
print(numbers_new)
print(len(numbers) - len(numbers_new))