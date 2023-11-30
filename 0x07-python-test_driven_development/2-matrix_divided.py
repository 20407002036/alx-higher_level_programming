#!/usr/bin/python3
"""Class definition
"""


def matrix_divided(matrix, div):
    """
    >>> test_mat = [[1, 2, 3], [4, 5, 6]]
>>> div_mat = __import__('2-matrix_divided').matrix_divided
>>> print(div_mat(test_mat, 2))
[0.5, 1.0, 1.5, 2.0, 2.5, 3.0]

>>> test_mat = [['a', 'b', 'c'], [4, 5, 6]]
>>> print(div_mat(test_mat, 2))
Traceback (most recent call last):
	...
TypeError: matrix must be a matrix (list of lists) of integers/floats

>>> test_mat = [[0, 1, 2], [4, 5, 6]]
>>> print(div_mat(test_mat, "TheOne"))
Traceback (most recent call last):
	...
TypeError: div must be a number

>>> test_mat = [[0, 1, 2], [4, 5, 6]]
>>> print(div_mat(test_mat, 0))
Traceback (most recent call last):
	...
ZeroDivisionError: division by zero


>>> test_mat = [[0, 1, 2, 90, 30], [4, 5, 6]]
>>> print(div_mat(test_mat, 2))
Traceback (most recent call last):
	...
TypeError: Each row of the matrix must have the same size

    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
        return matrix
    elif div == 0:
        raise ZeroDivisionError("division by zero")
        return matrix

    prevRowLen = -1
    new_list = []
    for row in matrix:
        if (prevRowLen != len(row) and prevRowLen != -1):
            raise TypeError("Each row of the matrix must have the same size")
            return matrix
        for ele in row:
            if not isinstance(ele, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of" +
                                " integers/floats")
                return matrix
            else:
                new_list.append(round(ele / div, 2))
        prevRowLen = len(row)

    return new_list
