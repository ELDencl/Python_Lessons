# Напишите программу, которая на вход принимает два числа и проверяет, является ли второе число квадратом первого.
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if b == a**2 :
    print(f"число {b} является квадратом числа {a}")
else :
    print(f"число {b} не является квадратом числа {a}")
