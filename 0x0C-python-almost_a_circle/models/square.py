#!/usr/bin/python3
"""Module square.
Create a Square class, inheriting from Rectangle.
"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class describing a square.
    Public instance methods:
        - area()
        - display()
        - to_dictionary()
        - update()
    Inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance.

        Args:
            - __size: size
            - __x: position
            - __y: position
            - id: id
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of a Square instance."""

        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Retrieves the size attribute."""

        return self.width

    @size.setter
    def size(self, value):
        """Sets the size attribute."""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Updates the instance attributes from
        the arguments passed in a strict order
        or from the kwargs
        '''
        i = 0
        attributes = ['id', 'size', 'x', 'y']
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
        """Returns the dictionary representation of a Square."""

        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
