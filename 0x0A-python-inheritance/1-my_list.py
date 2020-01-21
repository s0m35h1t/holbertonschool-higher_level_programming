#!/usr/bin/python3
"""Defines: class MyList"""


class MyList(list):
    """Represents a MyList

    Attributes:
        None
    """

    def __init__(self):
        """Initializes a List

        Args:
            None

        Returns: None
        """
        super().__init__

    def print_sorted(self):
        """print sorted list

        Args:
            None

        Returns: None
        """
        print(sorted(self))
