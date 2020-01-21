#!/usr/bin/python3


Rectangle = __import__('9-rectangle').Rectangle
"""Define: Square class"""


class Square(Rectangle):
    """Represents a Square

    Attributes:
        __width (int): rectangle width
        __height (int): rectangle height
    """

    def __init__(self, size):
        """Initializes a Square

        Args:
            width (int): square width
            heigth (int): square heigth

        Returns: None
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """calculates the square's area
        Returns:
            (int) The area of the rectangle
        """
        return self.__size ** 2

    def __str__(self):
        """printable string representation of the square

        Args:
            None

        Returns:
            string
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
