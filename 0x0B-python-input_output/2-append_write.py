#!/usr/bin/python3
"""Write a function that appends a string to the end of text file"""


def append_write(filename="", text=""):
    """Appends a string to a text file"""

    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(text)

    return len(text)
