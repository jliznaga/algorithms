def longest_binary_gap(n: int) -> int:
    count = 0
    max_count = 0
    can_count = False
    while n >= 2:
        print(bin(n).lstrip("0b"))
        if n % 2 == 0:
            if can_count:
                count += 1
        else:
            count = 0
            can_count = True
        if count > max_count:
            max_count = count
        n = n >> 1
    return max_count


print(longest_binary_gap(74901729))
