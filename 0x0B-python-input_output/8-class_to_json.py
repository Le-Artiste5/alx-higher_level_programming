#!/usr/bin/python3
"""Converts Python class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary represntation of a simple  structure of data."""

    return obj.__dict__
