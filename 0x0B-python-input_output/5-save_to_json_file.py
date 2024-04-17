#!/usr/bin/python3
"""Saving a json file for an object"""
import json

def save_to_json_file(my_obj, filename):
    """This function saves an object to a json file

    Args:
        my_obj: the object to be saved
        filename: The name of the file to be saved in

    Return:
        rturns the written obj in the file
    """

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
