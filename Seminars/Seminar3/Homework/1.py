# Задача 1. Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8


def fibonachi():

    count = 0
    n =int(input("Введите колличество чисел для  вывода: "))

    numbers = [1,1]

    while count < n-2:
        numbers.append( numbers[count] + numbers[count+1])
        count += 1
    return numbers

print(fibonachi())