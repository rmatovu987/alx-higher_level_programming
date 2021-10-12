#!/usr/bin/python3
"""Write a function that creates an object from json file"""
import json


def load_from_json_file(filename):
    """Read a json file"""

    with open(filename, mode="r", encoding='utf-8') as f:
        return json.load(f)
