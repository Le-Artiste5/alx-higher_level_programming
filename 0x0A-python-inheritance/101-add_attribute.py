#!/usr/bin/python3
"""This project module is about inheritance"""

def add_attribute(obj, att, value):
    """This has attributes, obj, value

    Args:
        obj: This is an object
        att: attribute is ther
        value: The value

    Raises:
        TypeError: This is a type error 
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
