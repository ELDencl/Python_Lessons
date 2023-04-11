# 3. Напишите программу, которая будет на вход
# принимать число N и выводить числа от -N до N
# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

n = int(input("Введите число : "))
number = -n
n = abs(n)   # число по модулю 
if n > 0:
    while number != n + 1:
        print(number)
        number += 1
else:
    while number >= n:
        print(n)
        n += 1
