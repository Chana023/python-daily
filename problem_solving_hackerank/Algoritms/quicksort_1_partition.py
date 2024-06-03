# https://www.hackerrank.com/challenges/quicksort1/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    # Write your code here
    pivot = arr[0]

    left = []
    right = []

    for value in range(1,len(arr),1):
        if arr[value] < pivot:
            left.append(arr[value])
        if arr[value] > pivot:
            right.append(arr[value])

    left.append(pivot)

    arr = left + right

    print(*arr)
if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

