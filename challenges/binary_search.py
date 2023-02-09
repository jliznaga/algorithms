def binary_search(vector, n):
    down, up = 0, len(vector) - 1
    while down <= up:
        center = int((down + up) // 2)
        center_value = vector[center]
        if center_value == n:
            return center
        elif n < center:
            up = center - 1
        else:
            down = center + 1
    return -1


