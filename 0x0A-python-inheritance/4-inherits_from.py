#!/usr/bin/python3
"""This tasks checks if an object is an instance of a specified class"""

def inherits_from(obj, a_class):
    """This function checks if the object is an instance of a subclass

    Args:
        obj: The object itself
        a-class: This is the subclass to be checked

    Return:
        Returns true or false depending on the conditions
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
