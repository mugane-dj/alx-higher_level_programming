#!/usr/bin/python3

def print_square(size):
    """
    Prints a square
    Args:
    size(int): size lenght of the square.

    Raises:
        TypeError: if size is not an integer.
                   if size is a float and is less than 0.
        ValueError: if size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, int(size)):
        for j in range(0, int(size)):
            print("#", end="")
        print("")
    if size == 0:
        print("")
