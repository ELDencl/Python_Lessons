# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# spisok = [1, 2, 3, 4, 5, 8, 15, 23, 38]

# def chet(spisok):
#     for i in spisok:
#         if i % 2 == 0:
#             print(f"[{i},{i*i}]")


# chet(spisok)

data = [1, 2, 3, 5, 8, 15, 23, 38]
out = list()

for i in data :
    if i % 2 == 0:
        out.append((i, i ** 2))

print(out)


