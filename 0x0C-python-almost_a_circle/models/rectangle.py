#!/usr/bin/python3

"""Defines the Rectangle class Module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter function for width instance variable"""

        return self.__width

    @property
    def height(self):
        """Getter function for height instance variable"""

        return self.__height

    @property
    def x(self):
        """Getter function for x instance variable"""

        return self.__x

    @property
    def y(self):
        """Getter function for y instance variable"""

        return self.__y

    @width.setter
    def width(self, value):
        """Setter function for width instance variable"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter function for height instance variable"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter function for x instance variable"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter function for y instance variable"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Computes the area of a Rectangle instance"""

        area = self.__height * self.__width
        return area
