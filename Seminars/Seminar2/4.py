# Задача 4. Найдите все числа до 10000, у который количество делителей равно 10.

def zadacha4():
    count = 0
    for num in range(1, 10001):
        count_div = 0
        for div in range(1, num+1):
            if num % div == 0:
                count_div += 1
        if count_div == 10:
            count += 1
            print(num)
    print(f"Колличество чисел у которых 10 делителей равно : {count}")

zadacha4()
