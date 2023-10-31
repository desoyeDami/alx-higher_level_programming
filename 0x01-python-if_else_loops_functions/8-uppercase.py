#!/usr/bin/python3


def uppercase(str):
    res = ""
    for i in range(len(str)):
        if 97 <= ord(str[i]) <= 122:
            res += chr(ord(str[i]) - 97 + 65)
        else:
            res += str[i]
    print(res)
