#!/usr/bin/python3
"""This writes a function that inserts a line of text to a file"""

def append_after(filename="", search_string="", new_string=""):
    """This is the function and it has three arguments

    Args:
        filename: This is the name of the file we would be checking
        search_string:This would be the argument to handle searching if a string is styill there
        new_string: The neew string to be included

    Return:
        This returns a file with a new string attached
    """

    text = ""

    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as o:
        o.write(text)

