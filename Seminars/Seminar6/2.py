# Задача 2. Даны два случайных пятизначных числа.
# Определить, состоят ли они из одних и тех же цифр.


# 72426, 27624 –> да
# 44444, 44441 -> нет


def task2(num1: int, num2: int):
    nums1 = str(num1)
    list1 = [int(i) for i in nums1]
    list1.sort()

    nums2 = str(num2)
    list2 = [int(i) for i in nums2]
    list2.sort()

    if list1 == list2:
        print(f"число {num1} и число {num2} состоят из одних цифр")
    else:
        print(f"число {num1} и число {num2} состоят из разных цифр")



task2(12734, 48321)
