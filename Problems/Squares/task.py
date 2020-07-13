n = int(input())


def squares():
    i = 0
    while True:
        i += 1
        yield i ** 2


# Don't forget to print out the first n numbers one by one here
new_generator = squares()
for _ in range(n):
    print(next(new_generator))
