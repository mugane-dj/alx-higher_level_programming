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

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.height)

    @property
    def size(self):
        """Getter method for size of Square"""

        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size of Square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates each class attribute"""

        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x. self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = size
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
            i += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x. self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
