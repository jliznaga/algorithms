def find_intersection(input):
    str_1 = input[0]
    str_2 = input[1]
    set_1 = set(str_1.split(', '))
    set_2 = set(str_2.split(', '))
    intersertion = set_1.intersection(set_2)
    if len(list(intersertion)) == 0:
        return 'false'
    intersertion = sorted([int(n) for n in list(intersertion)])
    intersertion = [str(n) for n in intersertion]
    return ','.join(intersertion)


assert(find_intersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]) == "1,4,13")
assert(find_intersection(["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]) == "1,9,10")
