#!/usr/bin/python3
"""Module that defines Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class with custom string"""

    def __init__(self, size):
        """Initialize square"""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """String representation"""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
