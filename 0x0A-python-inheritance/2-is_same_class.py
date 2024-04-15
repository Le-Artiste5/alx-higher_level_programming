#!/usr/bin/python3
"""Fuction that returns true if the obj is an instance of specified class"""

def is_same_class(obj, a_class):
    """This function returns true or false

    Args:
        obj: The object of any type
        a_class: The class that matches the object instance

    Return:
        This returns true or false if object is an instance of the class
    """
    
    if type(obj) == a_class:
        return True
    else:
        return False
