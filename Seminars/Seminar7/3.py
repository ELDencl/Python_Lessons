# Задача 3: Создайте декоратор для метода нахождения суммы


# для конкретного числа аргументов
def our_format(func):
    def decorator(a, b):
        print(f"{a} + {b} = ", end='')
        func(a, b)
    return decorator


@our_format
def sum(a, b):
    print(a+b)


sum(3, 5)


def our_format2(func):
    def decorator(*args):
        for arg in args:
            print(f"{arg} + ", end='')
        print('\b\b= ', end='')
        func(*args)
    return decorator

@our_format2
def sum_4(a, b, c, d):
    print(a + b + c + d)


sum_4(4,5,6,0)
