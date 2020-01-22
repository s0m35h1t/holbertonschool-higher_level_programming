#!/usr/bin/python3
"""
Define: Strudent Class
"""


class Student:
    """Represents a Rectangle

    Attributes:
        first_name (str): student first name
        last_name (str): student last name
        age (int): student age
    """

    def __init__(self, first_name, last_name, age):
        """Initializes a rectangle

        Args:
        first_name (str): student first name
        last_name (str): student last name
        age (int): student age

        Returns: None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation of a Student instance
        with specified attributes
        Args:
            attrs (list): list of attributes names

        Returns:
            (Object) : dict
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for att in attrs:
            try:
                new_dict[att] = self.__dict__[att]
            except Exception:
                pass
        return new_dict
