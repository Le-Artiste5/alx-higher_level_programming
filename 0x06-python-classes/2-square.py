#!/usr/bin/python3

"""Defining a class Square"""

class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize the new square

        Args:
            size: The new size of the square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size
