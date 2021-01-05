#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    count_int = 0
    for value in range(x):
        try:
            print("{:d}".format(my_list[value]), end="")
        except (ValueError, TypeError):
            continue
        count_int += 1
    print("")
    return count_int
