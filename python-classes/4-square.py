#!/usr/bin/python3
"""Module containing the definition of the Square class."""


class Square:
    """An class that defines a square"""
    
    def __init__(self, size=0):
        """Initialize the Square with a given size."""
        self.__size = size

    @size.setter
    def size(self, value):
        """Setter method for the size attribute."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @size.self
    def size(self):
        """Getter method for the size attribute."""

        return self.__size

    def area(self):
        """Calculate and return the area of the square."""

        return self.__size ** 2
