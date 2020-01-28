#!/usr/bin/python3
"""Define: Rectangle Class"""

from models.base import Base


class Rectangle(Base):
    """Representation of Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization a Rectangle

        Args:
            width (int): Rectangle width
            height (int): Rectangle heigth
            x (int): Rectangle x position
            y (int): Rectangle y position
            id (int): Rectangle id

        Returns:
            None
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Rectangle width getter

        Args:
            None
        Returns:
            None
        """
        return self.__width

    @property
    def height(self):
        """Rectangle heigth getter

        Args:
            None
        Returns:
            None
        """
        return self.__height

    @property
    def x(self):
        """Rectangle x getter

        Args:
            None
        Returns:
            None
        """
        return self.__x

    @property
    def y(self):
        """Rectangle y getter

        Args:
            None
        Returns:
            None
        """
        return self.__y

    @width.setter
    def width(self, value):
        """Rectangle width setter

        Args:
            vlaue (int): rectangle new width
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Rectangle height setter

        Args:
            vlaue (int): rectangle new heigth
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Rectangle x setter

        Args:
            vlaue (int): rectangle new x
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Rectangle y setter

        Args:
            vlaue (int): rectangle new y
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return Rectangle area

        Args:
            None
        Returns:
            (int)
        """
        return self.__width * self.__height

    def display(self):
        """display Rectangle

        Args:
            None
        Returns:
            None
        """
        print(("\n" * self.__y) +
              "\n".join(((" " * self.__x) + ("#" * self.__width))
                        for _ in range(self.__height)))

    def __str__(self):
        """string represation of rectangle
        Args:
            None
        Return:
            (str)
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    def update(self, *args, **kwargs):
        """update rectanhgle attributes

        Args:
            None
        Returns:
            None
        """
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
        """retrun dictonary respersantaion of rectangle
        Args:
            None
        Returns:
            None
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
