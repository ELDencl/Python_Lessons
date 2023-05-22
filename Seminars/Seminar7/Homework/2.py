# Задача 2. Создайте декоратор, повторяющий функцию заданное количество раз.




def repeat(func):
    def decorator():
        i = 0
        count = int(input("введите колличестов повторений: "))
        while i < count:
            func()
            i += 1
    return decorator


@repeat
def adv():
    print("привет ")


adv()