#!/usr/bin/python3
"""[Module define the Rectangle class]
"""
from models.base import Base


class Rectangle(Base):
        """[Rectangle class

        Args:
            Base (Class): [Inherit from Base class]
        """

        def __init__(self, width, height, x=0, y=0, id=None):
                """[Define the __init__ method]
                """
                Base.__init__(self, id)
                self.width = width
                self.height = height
                self.x = x
                self.y = y

        """[Getter of width]
        """
        @property
        def width(self):
                return self.__width

        """[Setter of width]
        """
        @width.setter
        def width(self, width):
                if not isinstance(width, int):
                        raise TypeError("width must be an integer")
                elif width <= 0:
                        raise ValueError("width must be > 0")
                self.__width = width

        """[Getter of height]
        """
        @property
        def height(self):
                return self.__height

        """[Setter of height]
        """
        @height.setter
        def height(self, height):
                if not isinstance(height, int):
                        raise TypeError("height must be an integer")
                if height <= 0:
                        raise ValueError("height must be > 0")
                self.__height = height

        """[Getter of x]
        """
        @property
        def x(self):
                return self.__x

        """[Setter of x]
        """
        @x.setter
        def x(self, x):
                if not isinstance(x, int):
                        raise TypeError("x must be an integer")
                elif x < 0:
                        raise ValueError("x must be > 0")
                self.__x = x

        """[Getter of y]
        """
        @property
        def y(self):
                return self.__y

        """[Setter of y]
        """
        @y.setter
        def y(self, y):
                if not isinstance(y, int):
                        raise TypeError("y must be an integer")
                elif y < 0:
                        raise ValueError("y must be > 0")
                self.__y = y

        def area(self):
                """[Method area return the area of the Rectangle]
                """
                return self.__width * self.__height

        def display(self):
                """[Method display print spaces and '#' character]
                """
                print(('\n' * self.y) + ((' ' * self.x) + ('#' * self.width +
                                         '\n')) * self.height, end="")

        def __str__(self):
                """[__str__, overriding the __str__ method so that it returns:
                        [Rectangle] (<id>) <x>/<y> - <width>/<height>]
                """
                return '[{}] ({}) {}/{} - {}/{}'.format(Rectangle.__name__,
                                                        self.id,
                                                        self.__x,
                                                        self.__y,
                                                        self.width,
                                                        self.height)

        def update(self, *args, **kwargs):
                """[Update method update de values of the class attributes]
                """
                atr = ['id', 'width', 'height', 'x', 'y']
                if args and args[0] is not None:
                        for i in range(len(args)):
                                setattr(self, atr[i], args[i])
                else:
                        for key in kwargs:
                                setattr(self, key, kwargs[key])

        def to_dictionary(self):
                """[Return dic]
                """
                return self.__dict__
