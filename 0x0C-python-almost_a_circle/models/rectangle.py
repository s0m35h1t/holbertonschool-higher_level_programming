#!/usr/bin/pyhton3
"""Define: Rectangle Class"""

from models.base import Base


class Rectangle(Base):
    """"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """"""
        return self.__width

    @property
    def height(self):
        """"""
        return self.__height

    @property
    def x(self):
        """"""
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        """"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """"""
        return self.__width * self.__height

    def display(self):
        """"""
        print(("\n" * self.__y) +
              "\n".join(((" " * self.__x) + ("#" * self.__width))
                        for _ in range(self.__height)))

    def __str__(self):
        """"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    def update(self, *args, **kwargs):
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                        if hasattr(self, key) is True:
                            setattr(self, key, value)

    def to_dictionary(self):
        """"""
        return {
            "id": self.id,
            "width": self.width,
            "heigth": self.height,
            "x": self.x,
            "y": self.y
        }