#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    "Computes the square of each integer in a matrix"
    return ([list(map(lambda x: x ** 2, row)) for row in matrix])
