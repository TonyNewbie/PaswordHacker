import itertools

for first_name, middle_name in itertools.product(first_names, middle_names):
    print(first_name, middle_name)
