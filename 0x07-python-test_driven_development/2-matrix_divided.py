#!/usr/bin/python3

""" matrix function"""


def matrix_divided(matrix, div):
    """ matrix function

    args
        matrix: matrix
        div: division
    return
        division
    """
    matrice = []
    length = len(matrix[0])
    ln = len(matrix)
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in matrix for num in row])):
                raise TypeError("matrix must be a matrix \
                        (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        liste = []
        for i in row:
            res = round(i / div, 2)
            liste.append(res)
        matrice.append(liste)
    return matrice
