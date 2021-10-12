#!/usr/bin/python3
""" Student Class """


class Student:
    """
    # Defines a student.

    Args:

        first_name (string) = First name.
        last_name (string) = Last name.
        age (int) = Age.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance. """

        attributes = {}
        exits = 0

        if type(attrs) == list:

            for item in attrs:

                if type(item) != str:
                    exits = 1
                    break

                for key, value in self.__dict__.items():
                    if key == item:
                        attributes[key] = value

            if exits == 0:
                return (attributes)

        return (self.__dict__)

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance. """

        for key, value in json.items():
            setattr(self, key, value)
