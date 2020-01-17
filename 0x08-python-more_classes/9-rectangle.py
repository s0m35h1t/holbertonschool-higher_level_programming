#!/usr/bin/python3
"""
Defines: class Rectangle
"""


class Rectangle:
    """Represents a Rectangle

    Attributes:
        width (int): rectangle width
        height (int): rectangle height
        number_of_instances (int): number of instances
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a rectangle

        Args:
            width (int): rectangle width
            height (int): rectangle height

        Returns: None
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get rectangle width

        Returns:
            Private instance attribute __width
        """
        return self.__width

    @property
    def height(self):
        """rectangle height

        Returns:
            Private instance attribute __height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """set of rectangle width

        Args:
            value (int): the width value of the rectangle

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """set of rectangle height

        Args:
            value (int): the height value of the rectangle

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates the rectangle's area
        Returns:
            The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """calculates the rectangle's perimeter
        Returns:
            The perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compare two rectangle based on the area

        Args:
            rect_1 (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle

        Returns:
            Rectangle
        """
        if rect_1 is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if rect_2 is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """new Rectangle instance that is a square height == width

        Args:
            cls (class): class type
            size (int): square size

        Returns:
            string
        """
        return cls(size, size)

    def __str__(self):
        """printable string representation of the rectangle

        Args:
            None

        Returns:
            string
        """
        rep_str = ""
        if self.__width != 0 and self.__height != 0:
            rep_str += "\n".join(str(self.print_symbol) * self.__width
                                 for i in range(self.__height))

        return rep_str

    def __repr__(self):
        """return string representation of the rectangle

        Args:
            None

        Returns:
            string
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a string when an instance has been deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
