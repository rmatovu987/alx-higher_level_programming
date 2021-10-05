#!/usr/bin/python3
"""Write a function magic string"""


def magic_string(n=[0]):
    n[0] += 1
    return str("BestSchool, " * (n[0] - 1)) + "BestSchool"
