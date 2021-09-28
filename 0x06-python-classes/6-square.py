#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """Write a class that defines a square by: (based on 2-square.py)"""
    def __init__(self, size=0, position=0):
        self.__size = size
        self.__position = position

    """Calculates the area"""
    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size
    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise ValueError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        import sys
        if self.__size == 0:
            print()
        else:
            if self.__position[0] != 0:
                print("\n" * self.__position[1], end="")
            for t in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size, file=sys.stdout)
