#!/usr/bin/python3
"""
Contains the class MyInt
"""


class MyInt(int):
    """
    A custom integer class that inherits from the built-in int class 
    with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Override the equality operator (==).

        Parameters:
            other: The value to compare with.

        Returns:
            bool: True if the values are not equal; otherwise, False.
        """
        return (super().__ne__(other))

    def __ne__(self, other):
        """
        Override the inequality operator (!=).

        Parameters:
            other: The value to compare with.

        Returns:
            bool: True if the values are equal; otherwise, False.
        """
        return (super().__eq__(other))
