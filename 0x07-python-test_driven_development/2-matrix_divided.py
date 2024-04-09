#!/usr/bin/python3
"""

This task handles the divsion of a matrix with an integer

"""

def matrix_divided(matrix, div):
    """This function divides a matrix with a float or ineger or an error is raised

    Args:
         matrix: The matrix to be divided
         div: The number used to divide

    Return: 
        Returns the matrix with int or floats
    
    Raises:
        TypeError: 
            This error is raised when a number isnt float or int
            if the list of matrix dont have same size
            if the elements in matrix isnt list
            if elements in list arent int or float
                    
    """
    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroErrorDivison("division by zero")

    msg_type = "matrix must be a matrix(list of lists) of integer/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    len_oto = 0
    msg_size = "Each row of the matrix must have the same size"

    for elemento in matrix:
        if not elemento or not isinstance(elemento, list):
            raise TypeError(msg_type)
        if len_oto != 0 and len(elemento) != len_oto:
            raise TypeError(msg_size)

        for num in elemento:
            if not type(num) in (int, float):
                raise TypeError(msg_type)
            len_oto = len(elemento)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
