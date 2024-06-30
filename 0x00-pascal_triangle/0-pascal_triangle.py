#!/usr/bin/python3
"""Pascal Triangle"""

def pascal_triangle(n):
    """
    a function that returns 
    a list of lists of integers 
    representing the Pascal triangle of n:
        => Returns an empty list if n <= 0
        => can assume n will be always an integer
    """
    pascal_triangle = []

    if n <= 0:
        return []

    for i in range(n):
        if (i == 0):
            pascal_triangle.append([1])
        else:
            cur_rows = []
            for j in range(i + 1):
                if (j == 0 or j == i):
                    cur_rows.append(1)
                else:
                    cur_rows.append(pascal_triangle[i - 1][j - 1] +
                                   pascal_triangle[i - 1][j])

            pascal_triangle.append(cur_rows)

    return (pascal_triangle)