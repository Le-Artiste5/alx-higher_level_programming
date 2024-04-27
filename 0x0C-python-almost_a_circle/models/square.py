#!/usr/bin/python3
""""This project deals with a new class called square"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """This is a class that inherits from rectangle"""


    def __init__(self, size, x=0, y=0, id=None):
        """"This a function that holds the arguments of the square

        Args:
            size: This is the size of the square
            x: This is the horizontal
            y: This is the vertical of the square
            id: This is the id
        """

        super().__init___(size, size, x, y, id )

        @property
        def size(self):
            """This is the size of the square"""
            return self.width

        @size.setter
        def size(self, value):
            self.width = value
            self.height = value

        def __str__(self):
            """The string representation"""
            return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
