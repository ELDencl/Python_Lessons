# Задача 3. Напишите программу вычисления арифметического 
# выражения заданного строкой. Используйте операции +,-,/,*. 
# приоритет операций стандартный.
# а) Решите задачу для одного действия;
# б) Дополнительное задание. Решите задачу для нескольких 
# действий;
# в) Решите задачу средствами python.


# 2+2 => 4
# 1+2*3 => 7



def task3():
    expression = input()



    if "+" in expression:
        a,b = map(float,expression.split("+"))
        print(a+b)
    elif "*" in expression:
        a,b = map(float,expression.split("*"))
        print(a*b)
    elif "-" in expression:
        a,b = map(float,expression.split("-"))
        print(a-b)
    elif "/" in expression:
        a,b = map(float,expression.split("/"))
        print(a/b)
    print(expression.split("+"))


   



task3()