#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print("{:d}".format(j), end=" " if j != i[-1] else "")
        print()
