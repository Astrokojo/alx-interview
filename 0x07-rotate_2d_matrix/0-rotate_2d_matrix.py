#!/usr/bin/python3
"""Description:
This module contains functions to rotate 2D matrices clockwise.

Usage:
- Call rotate_2d_matrix_180 to rotate a matrix 180 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """Rotate 2D matrix in-place"""
    N = len(matrix)
    # To rotate a square in place we transpose the matrix
    # and then reverse the rows

    # Transposing
    for i in range(N):
        for j in range(i + 1, N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reversing
    for i in range(N):
        matrix[i].reverse()
