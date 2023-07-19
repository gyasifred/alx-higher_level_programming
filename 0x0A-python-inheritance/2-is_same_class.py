#!/usr/bin/python3
"""Function to check if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """
    Check if the object is an instance of the specified class or its subclass.

    Parameters:
        obj (any): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if the object is an instance of the specified class or its subclass; otherwise, False.
    """
    return isinstance(obj, a_class)
