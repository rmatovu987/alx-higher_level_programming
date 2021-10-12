#!/usr/bin/python3
"""Write a function that writes an object to text file"""
import json


def save_to_json_file(my_obj, filename):
    """Write a function that writes to text file"""

    with open(filename, mode="w", encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
