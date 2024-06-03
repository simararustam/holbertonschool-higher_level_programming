#!/usr/bin/python3
"""This module provides a `Student` class to represent student
information and convert it into a dictionary format for easy
JSON serialization."""


class Student:
    """ A class to represent a student."""

    def __init__(self, first_name, last_name, age):
        """Constructs all the necessary attributes
        for the student object."""
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the student instance.
        """

        if attrs is None:
            return self.__dict__
        else:
            json_student = {}
            for atr in attrs:
                if atr in self.__dict__:
                    json_student[atr] = self.__dict__[atr]
            return json_student
