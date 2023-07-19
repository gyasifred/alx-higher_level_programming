#!/usr/bin/python3

def lookup(obj):
    """
    Get a list of attributes and methods of the given object.

    Parameters:
        obj (object): The object to inspect.

    Returns:
        list: A list containing the names of attributes and methods of the object.
    """
    return (dir(obj))
