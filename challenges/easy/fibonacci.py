def fibonacci(n):
    a, b = 0, 1
    while b <= n:
        print(a, end="")
        a, b = b, a + b


if __name__ == '__main__':
    fibonacci(8)
