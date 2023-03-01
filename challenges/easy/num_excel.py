def num_excel(number):
    res = ""
    while number > 0:
        number, reminder = divmod(number - 1, 26)
        res = chr(reminder + 65) + res
    return res


if __name__ == '__main__':
    print(num_excel(28))
