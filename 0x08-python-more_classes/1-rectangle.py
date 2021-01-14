#!/usr/bin/python3
"""[Module define class rectangle with a width and height]

Raises:
    TypeError: [If width is not an integer]
    ValueError: [If width is less than 0]
    TypeError: [If height is not an integer]
    ValueError: [If height is less than 0]

Returns:
    [None]: [No return]
"""


class Rectangle:
    """[Class define a rectangle with width and height]

    Raises:
        TypeError: [If width is not an integer
        ValueError: [If width is less than 0]
        TypeError: [If height is not an integer]
        ValueError: [If height is less than 0]

    Returns:
        [None]: [No return]
    """

    def __init__(self, width=0, height=0):

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
