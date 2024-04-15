#!/usr/bin/python3
"""This tasks inherits from a parent class"""


class MyList(list):
    """This class inherits from parent class"""

    def print_sorted(self):
        """This would print a list in sorted order"""
        print(sorted(self))

