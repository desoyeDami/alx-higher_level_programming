#!/usr/bin/python3
def max_integer(my_list=[]):
    res = 0
    i = 0
    while i < len(my_list) > 0:
        if res < my_list[i]:
            res = my_list[i]
        i += 1
    return res
