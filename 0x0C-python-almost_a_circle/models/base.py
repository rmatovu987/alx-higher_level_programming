#!/usr/bin/python3
"""This is the base of all other classes"""


class Base:
    """Base class for other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
