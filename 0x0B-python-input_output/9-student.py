#!/usr/bin/python3
""""Creating a class called student"""

class Student:
    """"This class contains the names of students"""

    def __init__(self, first_name, last_name, age):
        """This function contains keys in a class

        Args:
            first_name: This is the first name of a student in the class
            last_name: This is the last name of a student in a class
            age: This is the age of the student

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets the dictionary representation of a student"""
        return self.__dict__
