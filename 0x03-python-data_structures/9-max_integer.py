#!/usr/bin/python3
def max_integer(my_list=[]):
    list_len = len(my_list)
    if list_len < 1:
        return None
    else:
        res = 0
        i = 0
        while i < len(my_list):
            if res < my_list[i]:
                res = my_list[i]
            i += 1
        return res
