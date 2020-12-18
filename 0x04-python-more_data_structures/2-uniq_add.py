#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    for val in my_list:
        if val not in new:
            new.append(val)
    return sum(new)
