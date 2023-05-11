# Задача 3.
# Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.


def N(a, b):
    while b:
        a, b = b, a % b
    return a

for i in range(2, 12):
    for j in range(1, i):
        if N(i, j) == 1:
            print(f"{j} / {i}")