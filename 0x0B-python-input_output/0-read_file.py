#!/usr/bin/python3
"""Write a function that reads a text file and prints it to stdout"""


def read_file(filename=""):
    """Read a text file and prints it to stdout"""

    with open(filename, encoding='utf-8') as myFile:
        print(myFile.read(), end="")
