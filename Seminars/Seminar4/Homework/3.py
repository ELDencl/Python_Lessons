import math




# Задача 3. Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.

# 3 -> 3.142




def Round_pi(n):
    pi = math.pi
    return round(pi,n)

print(Round_pi(3))