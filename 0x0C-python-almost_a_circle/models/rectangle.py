#!/usr/bin/python3
"""Class rectangle inherited from Base"""
from models.base import Base


class Rectangle(Base):
    """Class rectangle inherited from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class initializer"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''retrieves the __width attribute value'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the new value to the __width attribute'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''retrieves the __height attribute value'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets the new value to the __height attribute'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''retrieves the __x attribute value'''
        return self.__x

    @x.setter
    def x(self, value):
        '''sets the new value to the __x attribute'''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''retrieves the __y attribute value'''
        return self.__y

    @y.setter
    def y(self, value):
        '''sets the new value to the __y attribute'''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Get the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Display the rectangle"""
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end='')
            for j in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """Return a string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        '''Updates the instance attributes from
        the arguments passed in a strict order
        or from the kwargs
        '''
        i = 0
        attributes = ['id', 'width', 'height', 'x', 'y']
        if len(args) > 0:
            for attr in attributes:
                if i > len(args) - 1:
                    break
                setattr(self, attr, args[i])
                i += 1
        else:
            for key, value in kwargs.items():
                if key not in attributes:
                    continue
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""

        return {'id': self.id, 'width': self.__width,
                'height': self.__height, 'x': self.__x, 'y': self.__y}
