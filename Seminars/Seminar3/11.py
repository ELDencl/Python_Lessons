import random


# Задача 1. В списке хранятся сведения о количестве осадков, выпавших за каждый день июня. Определите в какой период выпало больше осадков:
# в первой или второй половине июня.
# Примечание : список заполнить случайными числами от 0 до 25

days = 30
june = [random.randint(0, 25) for el in range(days)]

first_half = 0
second_half = 0

for i in range(days//2):
    first_half += june[i]

for j in range(days//2, days):
    second_half += june[j]

print(june)
print(first_half)
print(second_half)


if first_half > second_half:
    print("В первой половине июня больше осадков")
else:
    print("Во второй половине июня больше осадков")
