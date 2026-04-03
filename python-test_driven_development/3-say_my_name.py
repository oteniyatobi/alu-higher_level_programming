#!/usr/bin/python3
"""
Module 3-say_my_name
This module provides a function that prints a full name.
It validates that both first and last name arguments are strings.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first_name> <last_name>'.
    Raises TypeError if first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
