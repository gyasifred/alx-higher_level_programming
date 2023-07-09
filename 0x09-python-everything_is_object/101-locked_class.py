#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    A class that prevents the dynamic creation of new instance attributes,
      except for 'first_name'.
    """

    __slots__ = ['first_name']

    def __setattr__(self, attr, value):
        """
        Sets the value of the specified attribute if it is 'first_name', 
        otherwise raises an AttributeError.

        Parameters:
            attr (str): The name of the attribute to be set.
            value: The value to be assigned to the attribute.

        Raises:
            AttributeError: If the attribute being set is not 'first_name'.
        """
        if attr == 'first_name':
            self.__dict__[attr] = value
        else:
            raise AttributeError("Cannot create new instance attributes")
