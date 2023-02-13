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

    def display(self):
        """Prints the Rectangle instance with # in stdout"""

        if self.__width == 0 or self.__height == 0:
            print("")

        for i in range(self.__y, self.__y + self.__height):
            for j in range(self.__x, self.__x + self.__width):
                if ((i == self.__y or i == self.__y + self.__height - 1) or
                        (j == self.__x or j == self.__x + self.__width - 1)):
                    print("#", end="")
                else:
                    print(" ", end="")
            print("")

    def __str__(self):
        """Override __str__() from Base class"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates each class attribute"""

        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x. self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
            i += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x. self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of Rectangle"""

        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
