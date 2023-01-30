#!/usr/bin/python3

def add_integer(a, b=98):
    """
    This function adds two integers.

    Args:
    a(int): First number.
    b(int): Second number with a default of 98.

    Returns:
    int: The result of the sum of `a` and `b`.

    Raises:
        TypeError: If either a or b is a non-int or non-float arg.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
