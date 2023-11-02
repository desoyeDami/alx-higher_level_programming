#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    symbol = ":"
    arg = "arguments"
    if length - 1 == 0:
        symbol = "."
    if length - 1 == 1:
        arg = "argument"

    print(f"{length - 1} {arg}{symbol}")
    index = 1
    while index < length:
        print(f"{index}: {argv[index]}")
        index += 1
