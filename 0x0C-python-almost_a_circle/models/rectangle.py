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

        self.__width = value

    @height.setter
    def height(self, value):
        """Setter function for height instance variable"""

        self.__height = value

    @x.setter
    def x(self, value):
        """Setter function for x instance variable"""

        self.__x = value

    @y.setter
    def y(self, value):
        """Setter function for y instance variable"""

        self.__y = value
