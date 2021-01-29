#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for index, iter in enumerate(str):
        if index != n:
            new_str += iter
    return new_str
