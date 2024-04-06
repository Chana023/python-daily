# https://www.hackerrank.com/challenges/encryption/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here

    s_stripped = s.replace(" ","")
    length_of_stripped_str = len(s_stripped)
    sqrt_length = math.sqrt(length_of_stripped_str)

    rows = math.ceil(sqrt_length)
    columns = math.ceil(sqrt_length)

    grid_size = rows * columns

    grid = [s_stripped[i:i + columns] for i in range(0, grid_size, columns)]

    res = ''

    for col in range(len(grid[0])):
        res= res + ' '
        for row in range(len(grid)):
            try:
                res = res + grid[row][col]
            except IndexError:
                pass
            
    print(res.strip())
        

        

if __name__ == '__main__':

    s = input()

    result = encryption(s)

