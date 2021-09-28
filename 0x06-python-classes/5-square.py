#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """Write a class that defines a square by: (based on 2-square.py)"""
    def __init__(self, size=0):
        self.__size = size

    """Calculates the area"""
    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        import sys
        if self.__size == 0:
            print()
        else:
            for t in range(self.__size):
                print("#" * self.__size, file=sys.stdout)
