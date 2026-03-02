#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element at a specific index in a copy of a list."""
    # Create a copy of the original list
    new_list = my_list[:]
    
    # Check if the index is valid
    if 0 <= idx < len(my_list):
        new_list[idx] = element
    
    return new_list
