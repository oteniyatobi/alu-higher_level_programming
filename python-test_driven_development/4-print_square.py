#!/usr/bin/python3
"""
Module 4-print_square
This module provides a function that prints a square using the # character.
The size of the square is determined by the integer argument provided.
"""


def print_square(size):
    """
    Prints a square of '#' characters with the given size.
    Raises TypeError if size is not an integer or is a negative float.
    Raises ValueError if size is a negative integer.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
