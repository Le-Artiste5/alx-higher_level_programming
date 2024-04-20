#!/usr/bin/python3
"""A class that inherits from another parent class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Introduces a triangle in it"""

    def __init__(self, width, height):
        """This introduces a rectangle

         Args:
            self: The private instance method
            width(int): The width of the triangle
            height(int): The height of the triangle

        """

        self.integer_validator = ("width", width)
        self.__width = width
        self.integer_validator = ("height", height)
        self.__height = height
