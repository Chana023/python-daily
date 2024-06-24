# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort()

    result = []
    for index in range(len(arr)):
        x = abs(arr[index]-arr[index-1])
        result.append(x)

    print(min(result))

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)
