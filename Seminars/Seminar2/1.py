
def zadacha1():
    number = int(input("Введите число : "))

    print("Цикл for :")

    for i in range(1, number+1):
        if number % i == 0:
            if i % 2 == 0:
                print(f"{i}(чётное)")
            else:
                print(f"{i}(нечётное)")




zadacha1()