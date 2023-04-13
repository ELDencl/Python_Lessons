# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

# [-3, -2, -1, 0, 1, 2, 3]

def task():
    n = int(input("Введите число : "))
    numbers = []
    twist = 0
    for i in range(-n, n+1):
        numbers.append(i)
    for j in range(1, 3):
        numbers.insert(0, numbers[-1])
        numbers.pop()

    print(numbers)


task()
