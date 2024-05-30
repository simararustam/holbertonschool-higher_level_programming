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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle"""

    def __init__(self, width, height):
        """func is docced"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
