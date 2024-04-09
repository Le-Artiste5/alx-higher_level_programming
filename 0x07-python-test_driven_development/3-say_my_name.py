#!/usr/bin/python3
"""

This task prints the full name of a person

"""
def say_my_name(first_name, last_name=""):
    """This function prinsts the full name of a person

    Args:
        first_name = The first name of the person
        last_name = The last name of the person

    Return:
        This function returns the first and last name of this person

    Raises: 
        TypeError: with a message "first_name must be a string or last_name must be a string"

    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))



