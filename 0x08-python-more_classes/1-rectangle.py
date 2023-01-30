#!/usr/bin/python3

"""Define a class Rectangle"""


class Rectangle:
    """Definition of the rectangle"""

    def __init__(self, width=0, height=0):
        """Defines instance variables"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter function"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value
