# Описать свою пользовательскую функцию filter


def our_filter(func, numbers):
    return (el for el in numbers if func(el))



numbers = [4,6,7,14,97,3,465,2,9]

# print(list(filter(lambda x : x > 5, numbers)))

print(list(our_filter(lambda x : x > 5, numbers)))