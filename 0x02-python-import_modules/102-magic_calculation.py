#!/usr/bin/python3
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if a < b:
        add_result = add(a, b)
        c = add_result
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
