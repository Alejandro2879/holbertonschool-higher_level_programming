#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for iter in my_string:
        if iter != 'c' and iter != 'C':
            new_str = new_str + iter
    return new_str
