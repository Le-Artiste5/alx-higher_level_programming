#!/usr/bin/python3
"""This inherits fron the previous or parent class"""
Rectangle =  __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """This square inherits from the Ractangle"""

    def __init__(self, size):
        """This returns the size of a rectangle

        Args:
            size: This is the total size of the rectangle
        """

        self.integer_validator = ("size", size)
        super().__init__(size, size)
        self.__size = size
