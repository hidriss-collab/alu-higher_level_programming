#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        first = True
        for integer in row:
            if first:
                print("{:d}".format(integer), end="")
                first = False
            else:
                print(" {:d}".format(integer), end="")
        print()
