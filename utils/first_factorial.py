def first_factorial(num):
    if num == 1 or num == 0:
        return 1
    return num * first_factorial(num - 1)


assert first_factorial(4) == 24
assert first_factorial(8) == 40320
