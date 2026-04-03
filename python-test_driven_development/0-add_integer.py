#!/usr/bin/python3
"""
Module 0-add_integer
This module provides a function to add two integers.
It handles both integer and float inputs by casting floats to integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (cast to int) and returns the result.
    Raises TypeError if either argument is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
