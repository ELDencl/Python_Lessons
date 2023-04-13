# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2


def task():
    substring = input("Введите строку : ")
    pharse = input("Введите фразу : ")
    length_pharse = len(pharse)
    length_substring = len(substring)


    for i in range(length_substring):
        count = 0
        for j in range(length_pharse):
            if substring[i] == pharse[j]:
                count += 1
        print(f"{substring[i]} -> {count}")





task()        