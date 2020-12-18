#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = []
    for val in set_1:
        if val in set_1 and val not in set_2:
            new.append(val)
    for val in set_2:
        if val in set_2 and val not in set_1:
            new.append(val)
    return new
