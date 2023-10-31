#!/usr/bin/python3


def remove_char_at(str, n):
    i = 0
    res = ""
    for i in range(len(str)):
        if i != n:
            res += str[i]
    return res
