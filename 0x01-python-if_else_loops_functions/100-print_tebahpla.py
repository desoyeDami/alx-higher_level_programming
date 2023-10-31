#!/usr/bin/python3

n = 25
m = 0
while n != -1:
    if n % 2 != 0:
        m = n + 97
    else:
        m = n + 65
    alphabet = chr(m)
    print(f"{alphabet}", end="")
    n -= 1
