#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    add = 0
    index = 1
    while index < len(argv):
        add += int(argv[index])
        index += 1
    print(add)
