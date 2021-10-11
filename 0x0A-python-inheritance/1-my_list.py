#!/usr/bin/python3
"""Class inherits from list"""


class MyList(list):
    """Class my list"""

    def print_sorted(self):
        """Prints the list as a sorted list"""

        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
