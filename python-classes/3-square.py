#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initialize square with validated size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return the current square area"""
        return self.__size * self.__size
