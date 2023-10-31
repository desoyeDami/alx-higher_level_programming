#!/usr/bin/python3
n = 25
while n != -1:
    if n % 2 != 0:
        print(chr(n + 97), end="")
    else:
        print(chr(n + 65), end="")
    n -= 1
