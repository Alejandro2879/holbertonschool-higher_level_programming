#!/usr/bin/python3
"""Class square"""


class Square:
    """Class Square define private method size"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """area method compute the area of the square"""
    def area(self):
        return self.__size ** 2
