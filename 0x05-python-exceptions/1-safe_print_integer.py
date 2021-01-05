#!/usr/bin/python3
def safe_print_integer(value):
    ret = 0
    try:
        print("{:d}".format(value))
        ret = 1
    except ValueError:
        ret = 0
    return ret
