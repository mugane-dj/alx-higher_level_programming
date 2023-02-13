#!/usr/bin/python3

"""Defines the Square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Override __str__() from Rectangle class"""

        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                       self.x, self.y,
                                                       self.height)
