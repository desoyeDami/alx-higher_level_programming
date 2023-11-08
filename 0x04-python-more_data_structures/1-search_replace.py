#!/usr/bin/python3
def search_replace(my_list, search, replace):
    res = [replace if sch == search else sch for sch in my_list]
    return res
