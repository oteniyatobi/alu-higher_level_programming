#!/usr/bin/python3
"""
Module 5-text_indentation
This module provides a function that prints text with 2 new lines
after each occurrence of the characters '.', '?' and ':'.
Leading and trailing spaces on each printed line are removed.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?' or ':' character.
    Raises TypeError if text is not a string.
    No spaces at the beginning or end of each printed line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end='')
        if text[i] in '.?:':
            print('\n')
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            i += 1
