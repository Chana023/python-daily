# https://www.hackerrank.com/challenges/grid-challenge/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    sorted_grid = []

    for value in grid:
        temp_row = list(value)
        temp_row.sort()
        sorted_grid.append(temp_row)

    print(sorted_grid)

    for col in range(0, len(sorted_grid[0]),1):
        for row in range(1, len(sorted_grid)):
            if sorted_grid[row][col] < sorted_grid[row - 1][col]:
                return 'NO'
    return 'YES'
        

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)
