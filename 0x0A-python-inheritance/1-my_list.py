#!/usr/bin/python3

class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    Public Method:
        - print_sorted(): Returns a new list with elements sorted in ascending order (assuming all elements are of type int).

    Note:
    Since the built-in 'list' class already has a 'sort()' method, which sorts the list in place,
    we can simply use 'sorted(self)' to return a new sorted list without modifying the original list.
    """

    def print_sorted(self):
        """
        Returns a new list with elements sorted in ascending order (assuming all elements are of type int).

        Returns:
            list: A new list containing the elements of the original list sorted in ascending order.
        """
        return sorted(self)
