#!/usr/bin/python3

"""Defines a class Square"""


class Square:
    """Definition of the square"""

    def __init__(self, size=0, position=(0, 0)):
        """Defines instance variables"""

        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter function"""

        return self.__size

    @property
    def position(self):
        """Getter function"""

        return self.__position

    @size.setter
    def size(self, value):
        """Setter function"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Setter function"""
        if (not isinstance(value, tuple) or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square"""

        area = self.__size ** 2
        return area

    def my_print(self):
        """Prints the square to stdout"""

        for i in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
        if self.__size == 0:
            print("")
