#!/usr/bin/python3
"""Writing a python structure in json format"""
import json

def from_json_string(my_str):
    """Function that returns json object to string or so"""
    return json.loads(my_str)
