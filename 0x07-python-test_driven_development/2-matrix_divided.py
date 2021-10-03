#!/usr/bin/python3
"""Write a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Return new matrix after division"""

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    len_rows = []
    for row in matrix:
        len_rows.append(len(row))
    if not all(elem == len_rows[0] for elem in len_rows):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
