#!/usr/bin/python3

"""Defines a class Square"""


class Square:
    """Definition of the square"""

    def __init__(self, size=0):
        """Defines instance variables"""

        self.__size = size

        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            pass

    def area(self):
        """Calculates the area of the square"""

        area = self.__size ** 2
        return area
