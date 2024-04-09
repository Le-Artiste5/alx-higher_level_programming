#!/usr/bin/python3
"""

This code adds two integers that are either whole numbers or floats

"""

def add_integer(a, b=98):
    """Function that adds two integers or float numbers

    Args:
    a: This is the first number
    b: This is the second number

    Returns:
        The addition of these two given numbers

    Raises:
        TypeError: if a or b arent int or float

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError ("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError ("b must be an integer")

    a = int(a)
    b = int(b)
    return (a + b)
