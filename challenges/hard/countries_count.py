A = [[5, 4, 4], [4, 3, 4], [3, 2, 4], [2, 2, 2], [3, 3, 4], [1, 4, 4], [4, 1, 1]]
A = [[12345, 12345], [12345, 12345]]


def solution(A):
    rows = len(A)
    columns = len(A[0])
    countries_count = rows * columns
    for r in range(rows):
        for c in range(columns):
            if r + 1 < rows and A[r][c] == A[r + 1][c]:
                countries_count -= 1
            if c + 1 < columns and A[r][c] == A[r][c + 1]:
                countries_count -= 1

    return countries_count if countries_count > 0 else 1


print(solution(A))
