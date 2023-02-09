def longest_word(sen):
    words = sen.split()
    words = [''.join([item for item in w if item.isalnum()]) for w in words]
    maxx = max([(len(w), w) for w in words])
    return maxx[1]


assert longest_word('fun&!! time') == 'time'
assert longest_word('I love dogs') == 'love'
