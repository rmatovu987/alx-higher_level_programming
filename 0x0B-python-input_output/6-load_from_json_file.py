#!/usr/bin/python3
"""Write a function that creates an object from json file"""
import json


def load_from_json_file(filename):
    """Read a json file"""

    with open(filename, encoding='utf-8') as f:
        json.load(f.read())
