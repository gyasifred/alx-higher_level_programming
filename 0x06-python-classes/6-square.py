#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a Square"""

    def __init__(self, size=0, position=(0, 0)):
        ''' Initialise a new square class
        Args:
            size (int): The size of square
        '''
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def size(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(val, int) for val in value) or any(val < 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        '''Calculate Area of Square'''
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
