#!/usr/bin/python3
"""Function to check if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """return true if obj is the exact class a_class, otherwise false"""
    return (type(obj) == a_class)
