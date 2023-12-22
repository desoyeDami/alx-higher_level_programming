#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    #Get List length
    count = 0
    for _ in my_list:
        count+=1
    try:
        for num in range(0,x):
            print(my_list[num], end="")
        print()
    except IndexError:
        print()
        return count
    else:
        return x
