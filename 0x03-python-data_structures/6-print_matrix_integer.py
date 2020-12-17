#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for col in range(len(matrix)):
        space = ""
        for row in range(len(matrix[col])):
            print(space, end="")
            print("{:d}".format(matrix[col][row]), end="")
            space = " "
        print("")
