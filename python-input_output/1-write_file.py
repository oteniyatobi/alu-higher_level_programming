#!/usr/bin/python3
"""Writes a string to a file and returns number of characters"""

def write_file(filename="", text=""):
    """Write text to file and return number of characters"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
