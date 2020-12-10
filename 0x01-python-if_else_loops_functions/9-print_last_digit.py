#!/usr/bin/env python3
def print_last_digit(number):
    if number < 0:
        new_number = number * -1
        last = new_number % 10
        print('{}'.format(last), end='')
        return (last)
    else:
        new_number = number
        last = new_number % 10
        print('{}'.format(last), end='')
        return (last)
