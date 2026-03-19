#!/usr/bin/python3
"""Module that defines inherits_from function"""


def inherits_from(obj, a_class):
    """Returns True if obj is subclass of a_class (not same class)"""
    return isinstance(obj, a_class) and type(obj) is not a_class
