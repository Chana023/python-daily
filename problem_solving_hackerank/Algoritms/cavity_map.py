# https://www.hackerrank.com/challenges/cavity-map/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    # Write your code here
    n = len(grid)

    for x in range(1, n-1, 1):
        for y in range(1, n-1, 1):
            if grid[x][y] > grid[x-1][y] and grid[x][y] > grid[x+1][y] and grid[x][y] > grid[x][y-1] and grid[x][y] > grid[x][y+1]:
                templist_str = list(grid[x])
                templist_str[y] = 'X'
                grid[x] = ''.join(templist_str)
                
    print(grid)
    

if __name__ == '__main__':

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)
