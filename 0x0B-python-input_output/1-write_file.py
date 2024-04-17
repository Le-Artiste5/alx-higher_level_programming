#!/usr/bin/python3
"""writing a content into a file"""

def write_file(filename="", text=""):
    """This function writes a string and counts the number of charcters in it

    Args:
        filename: The file to be written into
        text: the text in the file

    Return: returns the number of characters in the file
    """

    with open(filename, "r+", encoding="utf-8") as f:
        return(f.write(text))
