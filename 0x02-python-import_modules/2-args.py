#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    symbol = ":"
    if length - 1 == 0:
        symbol = "."
    print(f"{length - 1} arguments{symbol}")
    index = 1
    while index < length:
        print(f"{index}: {argv[index]}")
        index += 1
