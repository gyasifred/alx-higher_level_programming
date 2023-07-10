#!/usr/bin/python3
'''Function to Add Integers'''


def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added. Defaults to 98.

    Returns:
        int: The addition of a and b, casted to an integer.

    Raises:
        TypeError: If a or b is not an integer or float.

    Notes:
        - If a or b is a float, it will be casted to an integer before the addition.
        - No external modules are used.


    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
