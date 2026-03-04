#!/usr/bin/python3
def safe_print_division(a, b):
    """Divide 2 integers and print result in finally."""
    result = None
    try:
        result = a / b
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
