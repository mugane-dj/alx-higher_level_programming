#!/usr/bin/python3

"""Defines the Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """Initializing constructor

        Args:
            width (int): the width of the Rectangle.
            height (int): the height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Computes the area of a rectangle"""
        area = self.__width * self.__height

        return area

    def __str__(self):
        """Returns the unofficial representation of the Rectangle"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
