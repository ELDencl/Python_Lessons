# Задача 1. Создайте пользовательский аналог метода map().


def our_map(func, numbers):
    return (func(el) for el in numbers)


numbers = [1, 2, 3, 4, 56, 7, 88, 8,]

print(list(our_map(lambda x: x+10, numbers)))
