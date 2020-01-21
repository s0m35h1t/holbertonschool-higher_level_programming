#!/usr/bin/python3


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Define: Rectangle class"""


class Rectangle(BaseGeometry):
    """Represents a Rectangle
    Bases:
        BaseGeometry (obj): BaseGeometry Class

    Attributes:
        __width (int): rectangle width
        __heigth (int): rectangle heigth
    """

    def __init__(self, width, height):
        """Initializes a Rectangle

        Args:
            width (int): rectangle width
            heigth (int): rectangle heigth

        Returns: None
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates rectangle area
        Args:
            None

        Returns:
            int
        """
        return self.__width * self.__height

    def __str__(self):
        """printable string representation of the rectangle

        Args:
            None

        Returns:
            string
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
