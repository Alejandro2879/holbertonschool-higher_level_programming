#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        len = 0
        for value in my_list:
            if len < x:
                len += 1

        for counter, value in enumerate(my_list):
            if counter < x:
                print(value, end="")
        print("")
    except TypeError:
        print("Error: x must be an integer")
    return len
