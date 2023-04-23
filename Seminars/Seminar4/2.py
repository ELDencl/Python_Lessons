


# На вход подаются два числа. Напишите метод, который вернёт сумму, разность, произведение и частное этих чисел.



def baza(a,b):
    return(a+b,a-b,a*b,a/b)


def raspak():
    a =3
    b =4
    summ, razznost, umnozhenie, delenie = baza(a,b)
    print(summ, razznost, umnozhenie, delenie)

print(baza(3,4))
raspak()




# def calc(num1, num2):
#     dictionary = {}
#     dictionary['Сумма чисел'] = num1 + num2
#     dictionary['Разность чисел'] = num1 - num2
#     dictionary['Произведение чисел'] = num1 * num2
#     dictionary['Частное чисел'] = num1 / num2
#     return dictionary

# number1 = int(input("Введите первое число: "))
# number2 = int(input("Введите второе число: "))
# dictionary = calc(number1, number2)

# for (k, v) in dictionary.items():
# print(k+":", v)