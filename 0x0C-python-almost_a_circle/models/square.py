#!/usr/bin/python3
"""Define: Rectangle Class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Representation of Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization a Square

        Args:
            size (int): sqaure size
            x (int): square x position
            y (int): square y position
            id (int): square id

        Returns:
            None
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Square size getter

        Args:
            None
        Returns:
            None
        """
        return self.width

    @size.setter
    def size(self, value):
        """Square size setter

        Args:
            value (int): square new size
        Returns:
            None
        """
        self.width = value
        self.height = value

    def __str__(self):
        """string represation of square
        Args:
            None
        Return:
            (str)
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        """update square attributes

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
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """retrun dictonary respersantaion of square
        Args:
            None
        Returns:
            None
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
