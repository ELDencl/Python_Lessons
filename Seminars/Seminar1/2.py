# Организуйте последовательный ввод чисел до тех
# пор, пока не будет введён 0. Подсчитайте среди введённых чисел те, которые кратны трём.

number = int(1)
count = 0

while number != 0:
    number = int(input("Введите число : "))
    if number % 3 == 0:
        count += 1

print(f"Колличество введенных цифр кратные трем равен {count}") 