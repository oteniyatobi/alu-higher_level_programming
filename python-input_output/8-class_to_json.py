#!/usr/bin/python3
"""Return dictionary description for JSON serialization"""


def class_to_json(obj):
    """Return dictionary of object attributes"""
    return obj.__dict__
