import itertools

for dishes, price in zip(itertools.product(main_courses, desserts, drinks),
                         itertools.product(price_main_courses, price_desserts, price_drinks)):
    if sum(price) <= 30:
        print(dishes[0], dishes[1], dishes[2], sum(price))
