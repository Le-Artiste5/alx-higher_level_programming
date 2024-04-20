#!/usr/bin/python3
"""Defines a class Student in the class."""


class Student:
    """Represent a student in a class."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student class

        Args:
            first_name: The first name of the student.
            last_name: The last name of the student.
            age: The age of the student.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {b: getattr(self, b) for b in attrs if hasattr(self, b)}
        return self.__dict__
    def reload_from_json(self, json):

        """Each students attribute should changed

        Args:
            json: The key/value pairs to replace attributes with.
        """
        for b, c in json.items():
            setattr(self, b, c)
