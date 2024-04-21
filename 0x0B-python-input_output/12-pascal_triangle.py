#!/usr/bin/python3
"""THis module writes a function taht writes a lists of lists for a pascal triangle"""


def pascal_triangle(n):
    """This function works with a list of lists for a pascal triangle

    Args:
        n: The sides of the triangle
    """
    
    if n <= 0:
        return []
    type(n) is int

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
