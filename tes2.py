S = "one+two-one-one+two+one"



def solution(S):
    i = 0
    numbers = []
    signs = []
    while i < len(S):
        if S[i : i + 3] == "one":
            numbers.append(1)
            i += 3
        elif S[i : i + 3] == "two":
            numbers.append(2)
            i += 3
        elif S[i] == "+":
            signs.append("+")
            i += 1
        elif S[i] == "-":
            signs.append("-")
            i += 1
        else:
            i += 1

    if numbers:
        sum = numbers[0]
    else:
        return 0

    for j in range(1, len(numbers)):
        if j - 1 < len(signs):
            if signs[j - 1] == "+":
                sum += numbers[j]
            elif signs[j - 1] == "-":
                sum -= numbers[j]

    return sum


print(solution(S))
