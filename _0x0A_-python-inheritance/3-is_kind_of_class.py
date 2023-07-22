#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of the specified class or its subclass.

    Parameters:
        obj (any): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if the object is an instance of the specified class or its subclass; otherwise, False.
    """
    return isinstance(obj, a_class)
