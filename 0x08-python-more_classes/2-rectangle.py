#!/usr/bin/python3
"""[Class define a rectangle with width and height]

Raises:
        TypeError: [If width is not an integer
        ValueError: [If width is less than 0]
        TypeError: [If height is not an integer]
        ValueError: [If height is less than 0]

Returns:
        [int]: [No return]
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
                self.width = width
                self.height = height

        @property
        def width(self):
                return self.__width

        @width.setter
        def width(self, width):
                if type(width) is not int:
                        raise TypeError("width must be an integer")
                elif width < 0:
                        raise ValueError("width must be >= 0")
                self.__width = width

        @property
        def height(self):
                return self.__height

        @height.setter
        def height(self, height):
                if type(height) is not int:
                        raise TypeError("height must be an integer")
                elif height < 0:
                        raise ValueError("height must be >= 0")
                self.__height = height

        def area(self):
                """[area]

                Returns:
                    [int]: [area of the rectangle]
                """
                return self.__width * self.__height

        def perimeter(self):
                """[perimeter]

                Returns:
                    [int]: [perimeter of the rectangle]
                """
                if self.__width is 0 or self.__height is 0:
                        return 0
                else:
                        return self.__width * 2 + self.__height * 2
