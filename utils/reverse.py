def reverse(arg):
    res = ""
    for i in range(len(arg), 0, -1):
        res += arg[i - 1]
    return res


assert reverse('webseiten') == 'netiesbew'
