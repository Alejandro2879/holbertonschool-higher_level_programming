#!/usr/bin/python3
    """[Module define the Square class]

    Raises:
        TypeError: [If size is not int]
        ValueError: [If size is less than 0]

    Returns:
        [Int]: [Area of the square]
    """


class Square:
    """[Class Square]
    """
    def __init_(self, size=0):
        self.size = size

        @property
        """[Getter of size]
        """
        def size(self):
            return self.__size

        """[Setter of size]
        """
        @size.setter
        def size(self, size):
            if type(size) is not int:
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size

        def area(self):
            """[Return the area of the square]
            """
            return self.__size ** 2
