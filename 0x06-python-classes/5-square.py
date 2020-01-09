#!/usr/bin/python3
"""Defines: class Square"""


class Square:
    """Represents a square

    Attributes:
        __size (int): size of a side of the square
    """

    def __init__(self, size=0):
        """Initializes a square

        Args:
            size (int): size of a side of the square

        Returns: None
        """
        self.__size = size

    def area(self):
        """calculates the square's area
        Returns:
            The area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """get squar size

        Returns:
            Private instance attribute __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """set of __size

        Args:
            value (int): the size of a size of the square

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """that prints in stdout the
        square with the character #

        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size, end="")
                print()
