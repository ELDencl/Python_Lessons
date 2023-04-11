# 5. Напишите программу, которая находит наибольшее и наименьшее число из списка значений

numbers =[1, 6, 60, 39, 67,-1, 5]

print(numbers[1])
print(max(numbers))
print(min(numbers))


min_value = numbers[0]
max_value = numbers[0]

for el in numbers :
    print(el)
    if el < min_value:
        min_value = el
    if el > max_value:
        max_value = el

print(f"максимальное число :{max_value}, минимальное число :{min_value}")

    
