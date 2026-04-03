#!/usr/bin/python3
"""
Module 2-matrix_divided
This module provides a function to divide all elements of a matrix.
Each element is divided by a given divisor and rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimal places.
    Raises TypeError if matrix is not a list of lists of integers/floats,
    if rows have different sizes, or if div is not a number.
    Raises ZeroDivisionError if div is zero. Returns a new matrix.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError(msg)
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(el / div, 2) for el in row] for row in matrix]
