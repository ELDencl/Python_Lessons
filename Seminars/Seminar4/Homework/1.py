

# Задача 1. Дано натуральное число N. Напишите метод, который вернёт список простых множителей числа N и количество этих множителей.

# 60 -> 2, 2, 3, 5


def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n // i
       i = i + 1
   if n > 1:
       primfac.append(n)
   return primfac
        
print(primfacs(60))
print(f'Колличество множителей равно {len(primfacs(60))}')
            
        
