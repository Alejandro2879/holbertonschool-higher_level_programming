#!/usr/bin/python3
"""
Mudule define function add_integer that add 2 numbers
"""


def add_integer(a, b=98):
    """ Funcion add a and b

    Args:
        a (int): [Firts number]
        b (int): [Second number]. Defaults to 98.

    Raises:
        TypeError: [If a is not an int or a float]
        TypeError: [If b is not an int or float]

    Returns:
        [int]: [Return a + b and cast the result to int]
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
