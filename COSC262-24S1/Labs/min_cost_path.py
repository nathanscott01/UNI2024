""""
Nathan Scott
COSC262 Lab 8
Minimum Cost Path
"""

import numpy as np
INFINITY = float('inf')  # Same as math.inf


def read_grid(filename):
    """Read from the given file an n x m grid of integer weights.
       The file must consist of n lines of m space-separated integers.
       n and m are inferred from the file contents.
       Returns the grid as an n element list of m element lists.
       THIS FUNCTION DOES NOT HAVE BUGS.
    """
    with open(filename) as infile:
        lines = infile.read().splitlines()

    grid = [[int(bit) for bit in line.split()] for line in lines]
    return grid


def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given
       grid of integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])

    cost_cache = {}

    # Cell Cost using cache
    def cell_cost(row, col):
        """The cost of getting to a given cell in the current grid."""
        if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
            return INFINITY  # Off-grid cells are treated as infinities
        elif (row, col) in cost_cache:
            return cost_cache[(row, col)]
        elif row == 0:
            min_cost = grid[row][col]
        else:
            min_cost = min(cell_cost(row - 1, col + delta_col) for
                           delta_col in range(-1, 2)) + grid[row][col]
        cost_cache[(row, col)] = min_cost
        return min_cost

    return min(cell_cost(n_rows - 1, col) for col in range(n_cols))

# def grid_cost(grid):
#     """Find the cheapest cost to get from row 1 to n-1 using a table"""
#     n_rows = len(grid)
#     n_cols = len(grid[0])
#     cost_table = np.zeros((n_rows, n_cols), dtype=int)
#
#     for i in range(n_rows):
#         for j in range(n_cols):
#             if i == 0:
#                 cost_table[i, j] = grid[i][j]
#             else:
#                 paths = []
#                 for delta_col in range(-1, 2):
#                     if 0 <= (j + delta_col) < n_cols:
#                         paths.append(cost_table[i - 1, j + delta_col])
#                 cost_table[i, j] = grid[i][j] + min(paths)
#     return min(cost_table[n_rows - 1])


def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return grid_cost(read_grid(filename))
