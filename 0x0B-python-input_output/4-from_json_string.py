#!/usr/bin/python3
"""Write a function that returns an Object from Json"""
import json


def from_json_string(my_str):
    """Read a JSON string"""

    return json.loads(my_str)
