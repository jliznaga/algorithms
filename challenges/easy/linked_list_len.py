def solution(A):
    value = A[0]
    length = 1
    while value != -1:
        length += 1
        value = A[value]
    return length


A = [1, 4, -1, 3, 2]
print(solution(A))
