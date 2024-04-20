#!/usr/bin/python3
""""This task develops from the previous cklass"""

class BaseGeometry:
    """This class is the parent class"""

    def area(self):
        """This particular function doesnt do much right now"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """This validates a value

        Args:
            self: This is the private instance
            name: The name of the value
            value: The type of value

        Raises:
            TypeError: this raises a type error
            ValueError: if value is less than a spoecific value

        Return:
            No return
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

