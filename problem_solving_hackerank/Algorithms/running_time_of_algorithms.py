# https://www.hackerrank.com/challenges/runningtime/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(arr):
    # Write your code here

    shift_count = 0

    for iterator in range(1, len(arr)):

        key_value = arr[iterator]
        k = iterator - 1

        while k >= 0 and key_value < arr[k]:
            arr[ k + 1] = arr[k]
            shift_count += 1
            k -= 1
        arr[k + 1] = key_value

    print(shift_count)

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

