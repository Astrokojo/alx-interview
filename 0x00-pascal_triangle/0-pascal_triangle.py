#!/usr/bin/python3
"""a function that returns
a list of lists of integers
representing the Pascal’s triangle of n """


def pascal_triangle(n):
    """function creates a pascal triangle"""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        triangle.append([])
        # n = 10. for 1 in ten triangle = [[]]
        # n = 10. for 2 in ten triangle = [[][]]
        triangle[i].append(1)
        if i > 0:
            for j in range(1, i):
                triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])
            triangle[i].append(1)

    return triangle

# print(pascal_triangle(5))
