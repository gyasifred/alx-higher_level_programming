#!/usr/bin/python3
class Base:
    """
    This is the base class for handling object identification.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new Base object.

        Parameters:
        - id (int, optional): The identification number for the object.
          If not provided, a unique identifier will be assigned.

        Attributes:
        - id (int): The identification number for the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
