#!/usr/bin/python3
"""Defines an inherited class MyList"""


class MyList(list):
    """Sorts printing for the built-in class inherited"""

    def  print_sorted(self):
        """Prints sorted integers in ascending order"""
        print(sorted(self))
