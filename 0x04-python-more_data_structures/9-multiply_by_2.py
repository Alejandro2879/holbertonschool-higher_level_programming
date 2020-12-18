#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = dict(a_dictionary)
    for val in new:
        new[val] = new[val] * 2
    return new
