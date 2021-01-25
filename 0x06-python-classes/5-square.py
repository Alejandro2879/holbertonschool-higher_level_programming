#!/usr/bin/python3
"""[Module defien de Square class]
"""


class Square:
        """[class recives a size and compute the area of a square
                and print it with the '#' character]
        """
        def __init__(self, size=0):
                self.size = size

        """[Getter size]"""
        @property
        def size(self):
                return self.__size

        """[Setter size]
        """
        @size.setter
        def size(self, size):
                if type(size) is not int:
                        raise TypeError("size must be an integer")
                elif size < 0:
                        raise ValueError("size must be >= 0")
                self.__size = size

        """[Return the area of the square]
        """
        def area(self):
                return self.__size

        """[Method print area off the square with the '#' char]
        """
        def my_print(self):
                if self.size == 0:
                        print()
                else:
                        print(('#' * self.__size + '\n') * self.__size, end="")
