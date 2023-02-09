def is_in(sub, input):
    return all([item in input for item in sub])


def min_window_substring(srt_arr):
    large_str = srt_arr[0]
    sub_str = srt_arr[1]
    index = 0
    while is_in(sub_str, ''.join(large_str)):
        large_str = large_str[1:]
        index += 1

    return large_str


assert min_window_substring(['ahffaksfajeeubsne', 'jefaa']) == 'aksfaje'
assert min_window_substring(['aaffhkksemckelloe', 'fhea']) == 'affhkkse'
