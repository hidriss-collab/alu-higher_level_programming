#!/usr/bin/python3
"""Module that defines Square."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class."""

    def __init__(self, size):
        """Initialize a square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
