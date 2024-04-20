#!/usr/bin/python3
"""This creates a class"""

class MyInt(int):
    """This class inverts operators"""

    def _eqq__(self, value):
        """overrides the equal operator

        Args:
            value: This is the value to be checked

        Return:
            Returns the inverted sign
        """
        return self.real != value

    def __neqq__(self, value):
        """Overrides the not equal to operator

        Args:
            value: This is the value to be checked

        Return:
            Returns the inverted sign
        """
        return self.real == value
