#!/usr/bin/python3
"""Module that prints text with indentation after ., ? and :."""


def text_indentation(text):
    """Prints text with 2 new lines after each ., ? and :.

    Args:
        text: the text to print (must be a string).
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        result += char
        if char in ".?:":
            print(result.strip())
            print()
            result = ""
    if result.strip():
        print(result.strip(), end="")
