#!/usr/bin/python3
"""Module that contains the add_integer function."""


def add_integer(a, b=98):
    """Add two integers.

    Args:
        a: The first integer or float.
        b: The second integer or float. Defaults to 98.

    Raises:
        TypeError: If a or b is not an integer or float.
        OverflowError: If a or b is infinity.
        ValueError: If a or b is NaN.

    Returns:
        The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
