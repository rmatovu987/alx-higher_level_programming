#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """Write a class that defines a square by: (based on 2-square.py)"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """Calculates the area"""
    def area(self):
        return self.__size ** 2
