# https://www.hackerrank.com/challenges/angry-children/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    
    arr = list(arr)
    arr.sort()

    mini = float('inf')

    for index in range(len(arr) - k + 1):
        current_unfairness = arr[index + k - 1]  - arr[index]
        if current_unfairness < mini:
            mini = current_unfairness

    print(mini)

if __name__ == '__main__':

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)
