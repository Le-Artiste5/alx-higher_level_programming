#!/usr/bin/python3
"""This project has to do with an instance of a class and an object"""


def is_kind_of_class(obj, a_class):
    """This checks if an object is an instance or inherited instance of a class

    Args:
        obj: This is the object
        a_class: This is the subclass that needs to be checked

    Return:
        This returns true or false if an object is an instance of a subclass

    """
    if isinstance(obj, a_class):
        return True
    else:
        return False

