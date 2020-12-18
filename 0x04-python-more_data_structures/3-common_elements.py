#!/usr/bin/python3
def common_elements(set_1, set_2):
    new = []
    for val in set_1:
        if val in set_1 and val in set_2:
            new.append(val)
    return new
