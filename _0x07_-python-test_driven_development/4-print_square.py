#!/usr/bin/python3
# 4-print_square.py
"""Defines a square-printing function."""


def print_square(size):
    """
    Prints a square of a given size using the character '#'.

    Parameters:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        TypeError: If size is a float and less than 0.

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(int(size)):
        [print("#", end="") for j in range(int(size))]
        print("")
