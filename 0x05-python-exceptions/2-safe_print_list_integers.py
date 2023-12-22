#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    item_count = 0
    for num in range(0, x):
        element = my_list[num]
        if isinstance(element, int):
            print("{:d}".format(element), end="")
            item_count += 1
    print()
    if x > item_count:
        return item_count
    else:
        return x
