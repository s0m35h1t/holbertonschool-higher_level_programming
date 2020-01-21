#!/usr/bin/python3


class MyInt(int):
    def __new__(cls, *args, **kwargs):
        """create new int

        Args:
            cls (object)

        Returns:
            int (object)
        """
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """equal operator
        Args:
            cls (object)

        Returns:
            int (object)
        """
        return int(self) != other

    def __ne__(self, other):
        """Not equal operator

        Args:
            cls (object)

        Returns:
            int (object)
        """
        return int(self) == other
