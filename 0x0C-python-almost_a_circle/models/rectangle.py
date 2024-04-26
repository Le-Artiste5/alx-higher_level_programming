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
            return (self.__width)

        @width.setter
        def width(self, value):
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """"This is the height of the rectabgle"""
            return (self.__height)

        @height.setter
        def height(self, value):
            if type(value) != int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value
        
        @property
        def x(self):
            """This is the horizontal coordinate"""
            return (self.__x)

        @x.setter
        def x(self, value):
            if type(value) != int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            """This is the vertical coordinate"""
            return (self.__y)

        @y.setter
        def y(self, value):
            if type(value) != int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

        def area(self):
            """This is the area of the rectangle"""
            return self.width * self.height

        def display(self):
            """This function displays the standard output of rectangle class"""
            for i in range(self.y):
                print()
            for i in range(self.height):
                print(" " * self.x + "#" * self.width)

        def __str__(self):
            """This overrrides str and print in a rectangle"""
            return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
        def update(self, *args, ***kwargs):
            """This function assigns an argument to each attribute"""
            
            if args:

                for count, arg in enumerate(args):
                    if count == 0:
                        self.id = arg
                    elif count == 1:
                        self.width = arg
                    elif count == 2:
                        self.height = arg
                    elif count == 3:
                        self.x = arg
                    elif count == 4:
                        self.y - arg
                    else:
                        continue
            elif len(kwargs) > 0:
                for key, value in kwargs.items():
                    if key == "ïd":
                        self.id = value
                    elif key == "width":
                        self.width = value
                    elif key == "height":
                        self.height = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value
                    else:
                        break


