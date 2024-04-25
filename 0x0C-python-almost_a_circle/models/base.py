#!/usr/bin/python3
"""This talks about classses and so on"""
class Base:
    """This is a parent class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This is a function defined

        Args:
            id: id is the identification of attribute
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id =  Base.__nb_objects



