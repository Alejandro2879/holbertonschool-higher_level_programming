#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for iter in str:
        if ord(iter) >= 97 and ord(iter) <= 122:
            new_str += chr(ord(iter) - 32)
        else:
            new_str += iter
    print(new_str)
