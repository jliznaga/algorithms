def questions_marks(input):
    num_founded = False
    sub_strs = []
    tmp_str = ""
    for item in input:
        if num_founded:
            tmp_str += item

        if item.isnumeric():
            num_founded = not num_founded
            if tmp_str != "":
                sub_strs.append(tmp_str)
                tmp_str = ""

    if all(item.count('?') >= 3 for item in sub_strs):
        return 'true'
    return 'false'


assert questions_marks('aa6?9') == 'false'
assert questions_marks('acc?7??sss?3rr1??asdasd?5') == 'true'
