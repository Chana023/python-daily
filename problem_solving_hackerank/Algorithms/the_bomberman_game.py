# https://www.hackerrank.com/challenges/bomber-man/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    # Write your code here
    if n == 1:
        #No changes
        return grid
    if n%2 == 0:
        #All spaces have bombs
        return ["O"*c for _ in range(r)]
    pattern = re.compile(r'(?=O)')
    #There are two patterns for each odd number after 1
    #Pattern is determined by "(n//2) % 2"
    for _ in range(2 - (n//2)%2):
        detonations = set()
        #Get the locations of the detonations
        for match in pattern.finditer("\n".join(grid)):
            y = match.start()//(c+1)
            x = match.start()%(c+1)
            detonations.add((y, x))
            if y != 0:
                detonations.add((y-1, x))
            if y != r-1:
                detonations.add((y+1, x))
            if x != 0:
                detonations.add((y, x-1))
            if x != c-1:
                detonations.add((y, x+1))
        grid = ["" for _ in range(r)]
        for y in range(r):
            for x in range(c):
                if (y,x) in detonations:
                    grid[y] += "."
                else:
                    grid[y] += "O"
    return grid

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)
