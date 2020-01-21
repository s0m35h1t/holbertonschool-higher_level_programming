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

    def __init__(self, width, heigth):
        """Initializes a Rectangle

        Args:
            width (int): rectangle width
            heigth (int): rectangle heigth

        Returns: None
        """
        self.integer_validator("width", width)
        self.integer_validator("heigth", heigth)
        self.__width = width
        self.__heigth = heigth
