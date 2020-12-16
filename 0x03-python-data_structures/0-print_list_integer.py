#!/usr/bin/python3


def print_list_integer(my_list=[]):
    iter = 0
    while iter < len(my_list):
        print("{0:d}".format(my_list[iter]))
        iter += 1
