#!/usr/bin/python3

"""Define a class Rectangle"""


class Rectangle:
    """Definition of the rectangle"""

    def __init__(self, width=0, height=0):
        """Defines instance variables"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter function"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Getter function"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Computes the area of a rectangle"""
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """Computes the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Returns the unofficial representation of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return rect

    def __repr__(self):
        """Returns the official string representation of the Rectangle"""
        
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self:
        """Deletes an instance of Rectangle class"""
        print("Bye rectangle...")
