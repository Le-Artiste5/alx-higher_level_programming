#!/usr/bin/python3
"""This project handles writing into a  file"""

def read_file(filename=""):
    """This reads a text file with an encoder stuff
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
