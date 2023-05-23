#!/usr/bin/python3


"""Defines a class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from parent BaseGeometry class"""

    def __init__(self, size):
        """Initializer of a Square instance

        Args:
            size (int): the size of a square side.
        """

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Computes the area of a Square instance"""
        area = self.__size ** 2
        return area

    def __str__(self):
        """Returns the unofficial representation of the Rectangle"""
        return "[Square] {}/{}".format(self.__size, self.__size)
