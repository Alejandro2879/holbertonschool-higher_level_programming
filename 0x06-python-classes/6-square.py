#!/usr/bin/python3
"""[Module defien de Square class]
"""


class Square:
        """[class recives a size and compute the area of a square
                and print it with the '#' character]
        """
        def __init__(self, size=0, position=(0, 0)):
                self.size = size
                self.position = position

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

        """[Getter of position]
        """
        @property
        def position(self):
                return self.__position

        """[Setter of position]
        """
        @position.setter
        def position(self, position):
                error = "position must be a tuple of 2 positive integers"
                if (type(position) != tuple or len(position) != 2 or
                        type(position[0]) is not int or position[0] < 0 or
                        type(position[1]) is not int or position[1] < 0):
                        raise TypeError(error)
                self.__position = position

        """[Return the area of the square]
        """
        def area(self):
                return self.__size ** 2

        """[Method print area off the square with the '#' char]
        """
        def my_print(self):

                if self.__size == 0:
                        print()
                else:
                        print('\n' * self.position[1], end="")
                        print("\n".join((" " * self.position[0]) + '#' *
                                        self.size for i in range(self.size)))
