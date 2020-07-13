def fibonacci(n):
    i = 0
    n0 = 0
    n1 = 1
    while i < n:
        if i == 0:
            yield n0
        elif i == 1:
            yield n1
        else:
            _sum = n0 + n1
            yield _sum
            n0 = n1
            n1 = _sum
        i += 1
