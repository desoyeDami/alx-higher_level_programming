#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    new_list = [element for element in my_list if isinstance(element, int)]
    list_len = sum(1 for _ in new_list)
    try:
        for num in range(0, x):
            print(new_list[num], end="")
        print()
        return x
    except IndexError:
        print()
        return list_len
