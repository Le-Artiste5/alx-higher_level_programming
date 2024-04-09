#!/usr/bin/python3
"""

This tasks handles the prinrinting of a square

"""
def print_square(size):
    """The size of a square to be printed, this function does that


    Args:
        size: This is the size of the square

    Return: 
        This returns a square of a fixed size

    Raises:
        if size isn't and integer, TypeError
        if size is less than zero, ValueError
        if size is less than zero or is a float, raise TypeError
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size is float:
        raise TypeError("size must be an integer")

    for a in range(size):
        print("#" * size)

