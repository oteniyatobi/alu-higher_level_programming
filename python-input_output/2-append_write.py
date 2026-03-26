#!/usr/bin/python3
"""Append text to a file"""


def append_write(filename="", text=""):
    """Append text and return number of characters added"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
