# Задача 4: Создайте декоратор с параметрами

def greetings(Hello):
    def our_greetings(func):
        def decorator():
            name = func()
            print(f"{Hello}, {name}")
        return decorator
    return our_greetings

@greetings("Привет")
def get_name():
    return input("Как тебя зовут? : ")



get_name()