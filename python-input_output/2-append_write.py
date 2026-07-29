#!/usr/bin/python3
"""Module that appends to a text file."""


def append_write(filename="", text=""):
    """Append a string to a UTF-8 text file."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
