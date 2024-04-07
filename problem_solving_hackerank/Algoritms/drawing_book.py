# https://www.hackerrank.com/challenges/drawing-book/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    midpoint = n // 2

    if p == midpoint:
        result = midpoint // 2
    elif p > midpoint:
        start = n
        result = (start - p) // 2
    elif p < midpoint:
        start = 0
        result = (p - start) // 2
    

    

    print(result)



if __name__ == '__main__':

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

  
