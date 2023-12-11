#!/usr/bin/python3
"""
Module for the Square class.
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle.

    Attributes:
    - size (int): The size of the square.
    - x (int): The x-coordinate of the square.
    - y (int): The y-coordinate of the square.
    - id (int): The identification number for the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square object.

        Parameters:
        - size (int): The size of the square.
        - x (int, optional): The x-coordinate of the square. Default is 0.
        - y (int, optional): The y-coordinate of the square. Default is 0.
        - id (int, optional): The identification number for the square.
                             If not provided, a unique identifier will be assigned.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size."""
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for size.

        Parameters:
        - value (int): The size value to set.

        Raises:
        - TypeError: If the provided value is not an integer.
        - ValueError: If the provided value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError('Size must be an integer')
        if value <= 0:
            raise ValueError("Size must be > 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
        - str: A string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
