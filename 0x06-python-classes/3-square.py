#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a Square"""

    def __init__(self, size=0):
        ''' Initialise a new square class
        Args:
            size (int): The size of square
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        '''Calculate Area of Square'''
        return self.__size ** 2
