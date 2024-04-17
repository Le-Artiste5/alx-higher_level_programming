#!/usr/bin/python
"""This module appends a string to an already existing content"""

def append_write(filename="", text=""):
    """This function appends to a file

    Args:
        filename(str): This is the name of the file
        text(str): the text to be added to the end

    Return:
        This returns the number of characters
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
