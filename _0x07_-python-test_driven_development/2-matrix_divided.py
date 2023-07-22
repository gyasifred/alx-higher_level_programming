#!/usr/bin/python3
# 2-matrix_divided.py
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Parameters:
        matrix (list): A list of lists representing the matrix.
                       Each element of the matrix must be an integer or float.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix with the elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    """

    # Check if matrix is a list of lists of integers or floats
    # if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) \
    #         or not all(isinstance(num, (int, float)) for row in matrix for num in row):
    #     raise TypeError(
    #         "matrix must be a matrix (list of lists) of integers/floats")

    # # Check if each row of the matrix has the same size
    # if not all(len(row) == len(matrix[0]) for row in matrix):
    #     raise TypeError("Each row of the matrix must have the same size")

    # # Check if div is a number (integer or float)
    # if not isinstance(div, (int, float)):
    #     raise TypeError("div must be a number")

    # # Check if div is equal to 0
    # if div == 0:
    #     raise ZeroDivisionError("division by zero")

    # # Divide each element of the matrix by div, rounded to 2 decimal places
    # new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    # return new_matrix
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
