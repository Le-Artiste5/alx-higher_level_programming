#!/usr/bin/python3
"""This creates a class"""

class MyInt(int):
    """This class inverts operators"""

    def _eqq__(self, value):
        """overrides the equal operator"""
        return self.real != value

    def __neqq__(self, value):
        """Overrides the not equal to operator"""
        return self.real == value
