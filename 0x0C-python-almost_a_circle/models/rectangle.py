#!/usr/bin/python3
"""
Module for the Rectangle class.
"""

from .base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from Base.

    Attributes:
    - width (int): The width of the rectangle.
    - height (int): The height of the rectangle.
    - x (int): The x-coordinate of the rectangle.
    - y (int): The y-coordinate of the rectangle.
    - id (int): The identification number for the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle object.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        - x (int, optional): The x-coordinate of the rectangle. Default is 0.
        - y (int, optional): The y-coordinate of the rectangle. Default is 0.
        - id (int, optional): The identification number for the rectangle.
                             If not provided, a unique identifier will be assigned.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width.

        Parameters:
        - value (int): The width value to set.

        Raises:
        - TypeError: If the provided value is not an integer.
        - ValueError: If the provided value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError('Width must be an integer')
        if value <= 0:
            raise ValueError("Width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height.

        Parameters:
        - value (int): The height value to set.

        Raises:
        - TypeError: If the provided value is not an integer.
        - ValueError: If the provided value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError('Height must be an integer')
        if value <= 0:
            raise ValueError("Height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Getter method for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for x.

        Parameters:
        - value (int): The x-coordinate value to set.

        Raises:
        - TypeError: If the provided value is not an integer.
        - ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Getter method for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for y.

        Parameters:
        - value (int): The y-coordinate value to set.

        Raises:
        - TypeError: If the provided value is not an integer.
        - ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
        - int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Display the rectangle with '#' characters.

        This method prints the rectangle to the standard output,
        taking into account the x and y coordinates.
        """
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
        - str: A string representation of the rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
