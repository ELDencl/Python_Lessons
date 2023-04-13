#Задача 2. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другую.
# qwe in qwertyqwe -> 2 раза

def zadacha2():
    substring = input("Введите строку : ")
    pharse = input("Введите фразу : ")
    length_substring = len(substring)
    length_pharse = len(pharse)
    count = 0

    for i in range(length_pharse):
        if pharse[i:i+length_substring] == substring:
            count += 1
           # print(pharse[i:i+length_substring])
    print(f'В фразе\n{pharse}\nподстрока {substring} встречается {count} раз ')




zadacha2()