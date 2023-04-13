# Задача 3. Дано число N. Заполните список длиной N элементами 1, -3, 9, -27, 81, -243...

def zadacha3(num):
    numbers = [1]
    while len(numbers) < num:
        numbers.append(numbers[-1]*-3)
    print(numbers)


def zadacha31(num):
    numbers = []
    for i in range(num):
        numbers.append((-3)**i)
    print(numbers)

zadacha3(5)
zadacha31(5)