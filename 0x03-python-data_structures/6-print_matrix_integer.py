#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for rw in matrix:
        for item in rw:
            print("{:d}".format(item), end=" ")
        print()
