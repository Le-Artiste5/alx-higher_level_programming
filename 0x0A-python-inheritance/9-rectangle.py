#!/usr/bin/python3
"""This module handles Rectangle based on the previous parent class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """This is a child class inheriting from parent"""

    def __init__(self, width, height):
        """This function validates the value of width and height

        Args:
            width(int): This is the width of the rectangle
            height(int): This is the height of the rectangle

        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """This is the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """This would return a printed string"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
