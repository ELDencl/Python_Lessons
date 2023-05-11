# Задача 4. Имеется 1000 рублей. Бык стоит – 100 рублей, корова – 50 рублей, телёнок – 5 рублей.
# Сколько быков, коров и телят можно купить на все эти деньги, если всего надо купить 100 голов скота?


# price = {"Бык": 100, "Корова": 50, "Теленок": 5}




budget = 1000
# bulls_count = 0
# cow_count = 0
# calf_count = 0
bulls_price = 100
cow_price = 50
calf_price = 5

bulls_count = budget // bulls_price
cow_count = budget // cow_price
calf_count = budget // calf_price


for bulls in range(bulls_count+1):
    for cows in range(cow_count+ 1):
        for calf in range(calf_count+1):
            if (calf + cows + bulls) == 100 and \
                bulls * bulls_price + cows * cow_price + calf * calf_price == 1000:
                print(f"Быков:{bulls}\nКоров:{cows}\nТелят:{calf}")