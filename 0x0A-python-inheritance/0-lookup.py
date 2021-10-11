#!/usr/bin/python3
"""Write a function that returns a list of available attributes"""


def lookup(obj):
    """Returns a list of attributes
    Args:
        -obj: The object to lookup
    """
    return dir(obj)
