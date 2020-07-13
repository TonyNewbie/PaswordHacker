n = int(input())


def even():
    i = 0
    while True:
        yield i
        i += 2


# Don't forget to print out the first n numbers one by one here
new_generator = even()
for _ in range(n):
    print(next(new_generator))
