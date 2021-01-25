#!/usr/bin/python3
""" Define the Square class"""


class Square:
    """[Class Square]"""
    def __init__(self, size=0):
        self.size = size

    """[Getter of size]"""
    @property
    def size(self):
        return self.__size

    """[Setter of size]"""
    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """[Return the area of the square]"""
    def area(self):
        return self.__size ** 2
