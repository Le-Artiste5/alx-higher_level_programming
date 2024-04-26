#!/usr/bin/python3
"""This projects helps the creation of a new class"""
from models.base import Base

class Rectangle(Base):
    """This class inherits from a parent class called base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This is the function that describes a rectangle

        Args:
            width: This is the width of the rectangle
            height: This is the height of the rectangle
            x: initial of a number
            y: Another initialization of the number
            id: This is the id

        Raises:
            TypeError: if the width or height isnt an integer
            ValueError: if either x or y < 0
            ValueError: if width of height is <= 0
            TypeError: if either x or y isn't an int
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
