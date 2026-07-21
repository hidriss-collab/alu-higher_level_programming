#!/usr/bin/python3
"""This module defines a Square class that can calculate its area."""


class Square:
    """Represent a square with size validation and area calculation."""

    def __init__(self, size=0):
        """Initialize a square and validate its size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
