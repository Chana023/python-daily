# https://www.hackerrank.com/challenges/minimum-distances/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    d = 0
    lowest_d = len(a)
    for value in range(len(a)):
        for y in range(len(a)):
            if a[value] == a[y] and value!=y:
                d = y - value
                if d < lowest_d:
                    lowest_d = d

    print(lowest_d)

if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

