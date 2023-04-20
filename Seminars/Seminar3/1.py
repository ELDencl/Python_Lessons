import random


# Задача 0. Дан список, заполненный случайными числами от 0 до 10. Определите, является ли сумма всех элементов чётной.


length = 7
# numbers = [0] * length

# for el in range(length):
#     numbers[el] = random.randint(0, 10)

# print(numbers)

numbers =[random.randint(0,10) for el in range(length)]
print(numbers)
sum = 0 
for index in range(length):
    sum += numbers[index]
print(f"сумма всех элементов равна {sum}")
if sum % 2 == 0:
    print('сумма четная')
else:
    print('сумма не четная')
