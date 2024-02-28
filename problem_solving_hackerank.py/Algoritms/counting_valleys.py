# https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    path_count = 0
    prev_path_count = 0
    valley = 0 

    for value in range(steps):
        if path[value] == 'U':
            path_count = path_count + 1
        elif path[value] == 'D':
            path_count = path_count - 1

        if prev_path_count == -1 and path_count ==0:
            valley = valley + 1

        prev_path_count = path_count

    print(valley)

        
        

if __name__ == '__main__':

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

