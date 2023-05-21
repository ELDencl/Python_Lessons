# Задача 2: создайте метод, позволяющий замерять время работы других методов.

# import time


def stopwatch(func):
    import time
    def decorator():
        start_time = time.time()
        func()
        print(f"Время выполнения {time.time() - start_time}")
    return decorator



@stopwatch   #декоратор
def our_math_str():
    # start_time = time.time()
    num = "132"
    result = int(num) + int(num*2) + int(num*3)
    print(result)
    # print(f"Время выполнения {time.time() - start_time}")

@stopwatch  #декоратор
def our_math_int():
    # start_time = time.time()
    num = 132
    result = num * 2 + num*100 + num * 2330004 + num * 1000000
    print(result)
    # print(f"Время выполнения {time.time() - start_time}")

our_math_str()
our_math_int()