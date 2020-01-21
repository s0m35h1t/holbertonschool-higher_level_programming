#!/usr/bin/python3
"""Defines: BaseGeometry Square"""


class BaseGeometry:
    """Represents a BaseGeometry

    Attributes:
        None
    """
    def area(self):
        """raise error
        Returns:
            The area of the square
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """that validates integer value
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
