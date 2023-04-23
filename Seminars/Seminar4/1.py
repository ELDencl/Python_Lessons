import random


# Создайте кортеж, заполненный случайными числами.
# Напишите метод, который заменяет элемент в кортеже по заданному индексу другим случайным числом.


numbers = (1, 2, 3, 4, 5, 6)


def Change(korteg, index):
    korteg = list(korteg)
    korteg[index] = random.randint(0,10)
    korteg = tuple(korteg)
    return korteg


print(numbers)
print(Change(numbers, 1))



# a = (1, 2, 5, 4, 9, 0)

# def change(item, index, value):
#     item = list(item)
#     item[index] = value
#     item = tuple(item)
#     return item

# print(change(a, 0, 121))




# Другой способ решения , через срезы 
def change_element(numbers, index):
    return numbers[:index] + (random.randint(1, 100), ) + numbers[index+1:]

numbers = tuple(random.randint(1, 100) for _ in range(10))
index = 2

print(numbers)
numbers = change_element(numbers, index)
print(numbers)
print(type(numbers))