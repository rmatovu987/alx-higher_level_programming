#!/usr/bin/python3
"""Write a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Write a string to a text file"""

    count = 0
    with open(filename) as f:
        for i in text:
            count += 1
        f.write(text)

    return count
