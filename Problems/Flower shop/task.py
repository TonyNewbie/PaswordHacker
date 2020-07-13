import itertools

for i in range(1, 4):
    for bouquets in itertools.combinations(flower_names, i):
        print(bouquets)
