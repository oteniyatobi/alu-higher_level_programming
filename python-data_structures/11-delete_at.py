#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Delete an item at a specific position in a list without using pop()."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    return my_list[:idx] + my_list[idx+1:]
