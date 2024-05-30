#!/usr/bin/python3
""" Geometry module"""


class BaseGeometry:
    """Exception"""

    def area(self):
        """fucn is docced"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """fucn is docced"""

        if not type(value) is int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
