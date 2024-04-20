#!/usr/bin/python3
"""Inherits another class"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """This square class that inherits from rectangle"""

    def __init__(self, size):
        """size of the square

        Arg:
            size: The size of the square
        """

        self.integer_validator = ("size", size)
        super().__init__(size, size)
        self.__size = size
