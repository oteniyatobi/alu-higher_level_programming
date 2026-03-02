#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Return a list of True/False indicating if each element is a multiple of 2."""
    result = []
    for num in my_list:
        result.append(num % 2 == 0)
    return result
