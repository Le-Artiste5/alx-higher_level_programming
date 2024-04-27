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

        def update(self, *args, **kwargs):
            """This is the argument attribute"""
            if args:
                for count, arg in enumerate(args):
                    if count == 0:
                        self.id = arg
                    if count == 1:
                        self.size = arg
                    if count == 2:
                        self.x = arg
                    if count == 3:
                        self.y == arg
                    else:
                        break

            elif len(kwargs) > 0:
                for key, value in kwargs.item():
                    if key == "id":
                        self.id = value
                    elif key == "size":
                        self.width = value
                        self.height = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value
                    else:
                        break
