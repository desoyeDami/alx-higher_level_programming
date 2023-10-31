#!/usr/bin/python3


def uppercase(str):
    for s in str:
        if 97 <= ord(s) <= 122:
            print("{}".format(chr(ord(s) - 97 + 65)), end="")
        else:
            print("{}".format(s), end="")
