def reversed_string(expression):
    result = list(expression)
    for i in range(len(result) // 2):
        temp = result[i]
        result[i], result[-(i + 1)] = result[-(i + 1)], temp

    return result


if __name__ == '__main__':
    print(reversed_string("aeiou"))
