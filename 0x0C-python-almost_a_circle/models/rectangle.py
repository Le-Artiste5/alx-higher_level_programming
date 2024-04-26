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

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            """This is the width of the rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            self.__width = value

        @property
        def height(self):
            """"This is the height of the rectabgle"""
            return self.__height

        @height.setter
        def height(self, value):
            self.__height = value
        
        @property
        def x(self):
            """This is the horizontal coordinate"""
            return self.__x

        @x.setter
        def x(self, value):
            self.__x = value

        @property
        def y(self):
            """This is the vertical coordinate"""
            return self.__y

        @y.setter
        def y(self, value):
            self.__y = value
