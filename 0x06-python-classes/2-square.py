#!/usr/bin/python3
"""Class square"""


class Square:
    """Square define private instance attribute: size and raise Exceptions"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
