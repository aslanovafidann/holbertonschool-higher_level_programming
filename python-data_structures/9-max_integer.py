#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max_val = my_list[0]  # ilk elementi ən böyük kimi qəbul edirik
    for i in my_list[1:]:  # siyahının qalan hissəsində dövr qururuq
        if i > max_val:
            max_val = i
    return max_val
