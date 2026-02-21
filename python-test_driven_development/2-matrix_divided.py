#!/usr/bin/python3
"""
Module for matrix_divided function.
This module provides a function to divide matrix elements.
It validates matrix structure and divisor.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.
    Returns new matrix with rounded results.
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_msg)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(err_msg)
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(err_msg)
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if div != div or div == float('inf') or div == float('-inf'):
        return [[0.0 for num in row] for row in matrix]
    return [[round(num / div, 2) for num in row] for row in matrix]
