#!/usr/bin/python3
"""Module that prints a square with the # character."""


def print_square(size):
    """Prints a square of # with the given size.

    Args:
        size: the size length of the square (int >= 0).
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
