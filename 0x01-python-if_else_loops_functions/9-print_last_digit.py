#!/usr/bin/env python3
def print_last_digit(number):
    cont = number
    if number < 0:
        new_number = cont * -1
    else:
        new_number = cont
    last = new_number % 10
    print(last, end='')
    return last
