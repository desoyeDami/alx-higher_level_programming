#!/usr/bin/python3
def weight_average(my_list=[]):
    numerator = sum([row[0] * row[1] for row in my_list])
    denominator = sum([row[1] for row in my_list])
    result = numerator / denominator
    return result
