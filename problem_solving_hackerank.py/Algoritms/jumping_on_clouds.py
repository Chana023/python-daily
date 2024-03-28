# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    i, jumps, clouds_len = 0, 0, len(c)
    while i < clouds_len - 1:
        jumps += 1
        if i < clouds_len - 2 and c[i + 2] == 0:
            i += 2
        else:
            i += 1
    return jumps


        

if __name__ == '__main__':

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

