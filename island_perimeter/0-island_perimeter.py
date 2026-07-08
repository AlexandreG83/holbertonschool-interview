#!/usr/bin/python3
"""
Module that computes the perimeter of an island.
"""

def island_perimeter(grid):
    """
    Return the perimeter of the island described in grid.
    """
    perimeter = 0
    len_grid = len(grid)
    for row in range(len_grid):
        for col in range(len_grid):
            if grid[row][col] == 1:
                perimeter += 4
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 1
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 1
                if row > 0 and grid[row + 1][col] == 1:
                    perimeter -= 1
                if col > 0 and grid[row][col + 1] == 1:
                    perimeter -= 1
    return perimeter