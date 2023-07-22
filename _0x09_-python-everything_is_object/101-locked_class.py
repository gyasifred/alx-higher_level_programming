#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    A class that prevents the dynamic creation of new instance attributes,
      except for 'first_name'.
    """

    __slots__ = ['first_name']
