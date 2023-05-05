from random import randint

# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке.
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают 
# Список уникальных элементов
# [1, 4, 2, 3, 6, 7]
def set_spisok():
    num = int(input("Введите количество элемнтов списка: "))
    spisok = [randint(1, 10) for _ in range(num)]
    print(spisok)
    spisok_set = set(spisok)
    print(f'{len(spisok) - len(spisok_set)} элемента свопадают')
    print("Список уникальных элементов")
    print(spisok_set)


set_spisok()