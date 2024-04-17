#!/usr/bin/python3
"""writing a content into a file"""

def write_file(filename="", text=""):
    """This function writes a string and counts the number of charcters in it
    Args:
        filename(str): The file to be written into
        text(str): the text in the file

    Return: 
        returns the number of characters in the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
