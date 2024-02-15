S = "ACCAABBC"

def solution(S):
    word = S
    while 'AA' in word or 'BB' in word or 'CC' in word:
        word = word.replace('AA', '')
        word = word.replace('BB', '')
        word = word.replace('CC', '')

    return word


print(solution(S))