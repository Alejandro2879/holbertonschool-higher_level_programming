#!/usr/bin/python3
from models.rectangle import Rectangle
"""[Module define the Square class]
"""


class Square(Rectangle):
        """[Square class that inherit from Rectangle]
        """
        def __init__(self, size, x=0, y=0, id=None):
                """[Define the __ini__ method]
                """
                super().__init__(size, size, x, y, id)

        @property
        def size(self):
                """[Getter of size]
                """
                return self.width

        @size.setter
        def size(self, size):
                """[Setter of size]
                """
                if not isinstance(size, int):
                        raise TypeError("width must be an integer")
                elif size <= 0:
                        raise ValueError("width must be > 0")
                self.width = size
                self.height = size

        def __str__(self):
                """[Print square with the '#' character]
                """
                return '[{}] ({}) {}/{} - {}'.format(Square.__name__,
                                                        self.id,
                                                        self.x,
                                                        self.y,
                                                        self.width)

        def update(self, *args, **kwargs):
                """[Update the attributes values]
                """
                lis_attr = ['id', 'size', 'x', 'y']
                if args and args[0] is not None:
                        for value in range(len(args)):
                                setattr(self, lis_attr[value], args[value])
                else:
                        for key in kwargs:
                                setattr(self, key, kwargs[key])

        def to_dictionary(self):
                """[Return dic]
                """
                return self.__dict__