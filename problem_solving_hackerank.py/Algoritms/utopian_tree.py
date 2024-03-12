# https://www.hackerrank.com/challenges/utopian-tree/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    height = 1

    if n == 0:
        return 1

    for cycle in range(1,n+1,1):
        if cycle % 2 != 0:
            height = height * 2
        elif cycle % 2 == 0:
            height = height + 1 

    print(height)

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)


