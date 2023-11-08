#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    first_set = list(set(set_1).difference(set_2))
    second_set = list(set(set_2).difference(set_1))
    total_dif_element = first_set + second_set
    return total_dif_element
