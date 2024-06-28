#!/usr/bin/python3
"""Island perimeter computing module.
"""


def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes.
    """
    if not grid or not isinstance(grid, list):
        return 0

    perimeter = 0
    rows = len(grid)

    for i in range(rows):
        cols = len(grid[i])
        for j in range(cols):
            if grid[i][j] == 1:
                # Check the four possible edges around the cell
                if i == 0 or grid[i-1][j] == 0:  # Top edge
                    perimeter += 1
                if j == cols - 1 or grid[i][j+1] == 0:  # Right edge
                    perimeter += 1
                if i == rows - 1 or grid[i+1][j] == 0:  # Bottom edge
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # Left edge
                    perimeter += 1

    return perimeter
