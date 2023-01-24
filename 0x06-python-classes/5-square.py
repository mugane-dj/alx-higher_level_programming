#!/usr/bin/python3

"""Defines a class Square"""


class Square:
    """Definition of the square"""

    def __init__(self, size=0):
        """Defines instance variables"""

        self.size = size

    @property
    def size(self):
        """Getter function"""

        return self.__size

    @size.setter
    def size(self, value):
        """Setter function"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square"""

        area = self.__size ** 2
        return area

    def my_print(self):
        """Prints the square to stdout"""
        for i in range(0, self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
