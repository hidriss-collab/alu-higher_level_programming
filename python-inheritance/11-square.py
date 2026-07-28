#!/usr/bin/python3
"""Module that defines Square."""

Square1 = __import__("10-square").Square


class Square(Square1):
    """Square class."""

    def __str__(self):
        """Return the square description."""
        return "[Square] {}/{}".format(self._Rectangle__width,
                                      self._Rectangle__height)
