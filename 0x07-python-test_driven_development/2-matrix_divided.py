#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix

    Args:
    matrix(list): A list of lists of integers or floats.
    div(int): Division factor.

    Returns:
        list: A new matrix.

    Raises:
        TypeError: if the matrix is not a list of lists.
                   if each row of the matrix is not the same size.
                   if div is not a number.
        ZeroDivisionError: if div is equal to zero.
    """

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(error_msg)

    new_matrix = []

    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(error_msg)
        if len(lists) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_list = []
        for num in lists:
            if not isinstance(num, (int, float)):
                raise TypeError(error_msg)
            new_list.append(round(num/div, 2))
        new_matrix.append(new_list)
    return new_matrix
