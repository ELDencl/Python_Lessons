# Задача 1. Дан список случайных элементов. Проверьте, что все его элементы уникальны.


n = [1, 2, 3, 4, 5, 6, 7, 8, 45, 23, 12, 2]


def set_n(n):
    n_new = set(n)
    if len(n) > len(n_new):
        print("Элементы не уникальны")
    else:
        print("Элементы уникальны")


print(n)

set_n(n)