# https://www.hackerrank.com/challenges/closest-numbers/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    arr.sort()

    diffs = []
    for value in range(1, len(arr), 1):
        diffs.append(arr[value] - arr[value - 1])

    min_diff = min(diffs)

    result = []

    for value in range(1, len(arr), 1):
        if arr[value] - arr[value - 1] == min_diff:
            result.append(arr[value -1 ])
            result.append(arr[value])

    print(*result)


if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)
