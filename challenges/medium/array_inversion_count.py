from itertools import combinations

A = [-1, 6, 3, 4, 7, 4]

# def solution(A):
#     count = 0
#     indexes = [i for i in range(len(A))]
#     comb = combinations(indexes, 2)
#     for c in comb:
#         if c[0] < c[1] and A[c[1]] < A[c[0]]:
#             count += 1

#     return count if count < 1000000000 else -1


def solution(A):
    count = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] < A[i]:
                count += 1

    return count if count < 1000000000 else -1


print(solution(A))
