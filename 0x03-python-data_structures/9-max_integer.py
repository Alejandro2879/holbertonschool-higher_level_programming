#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        max_int = my_list[0]
        for iter in my_list:
            if iter > max_int:
                max_int = iter
        return (max_int)
