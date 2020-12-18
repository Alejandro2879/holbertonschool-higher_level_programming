#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for iter, val in enumerate(new):
        if val == search:
            new[iter] = replace
    return new
