#!/usr/bin/python3
"""Module define the Rectangle class
"""
from models.base import Base


class Rectangle(Base):
        """Rectangle class inherits from Base class"""
        def __init__(self, width, height, x=0, y=0, id=None):
                """Define the __init__ method
                """
                Base.__init__(self, id)
                """[Call the __init__ method of the Base class]
                """
                self.width = width
                self.height = height
                self.x = x
                self.y = y

        @property
        def width(self):
                """[Getter method of width]
                """
                return self.__width

        @width.setter
        def width(self, width):
                """[Setter method of width]
                """
                if not isinstance(width, int):
                        raise TypeError("width must be an integer")
                elif width <= 0:
                        raise ValueError("width must be > 0")
                self.__width = width

        @property
        def height(self):
                """[Getter method of height]
                """
                return self.__height

        @height.setter
        def height(self, height):
                """[Setter method of height]
                """
                if not isinstance(height, int):
                        raise TypeError("height must be an integer")
                if height <= 0:
                        raise ValueError("height must be > 0")
                self.__height = height

        @property
        def x(self):
                """[Getter method of x]
                """
                return self.__x

        @x.setter
        def x(self, x):
                """[Setter method of x]
                """
                if not isinstance(x, int):
                        raise TypeError("x must be an integer")
                elif x < 0:
                        raise ValueError("x must be >= 0")
                self.__x = x

        @property
        def y(self):
                """[Getter method of y]
                """
                return self.__y

        @y.setter
        def y(self, y):
                """[Setter method of y]
                """
                if not isinstance(y, int):
                        raise TypeError("y must be an integer")
                elif y < 0:
                        raise ValueError("y must be >= 0")
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
