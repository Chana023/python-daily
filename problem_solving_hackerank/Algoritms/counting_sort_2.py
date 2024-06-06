# https://www.hackerrank.com/challenges/countingsort2/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    counting_arr = [0] * 100

    for value in arr:
        counting_arr[value] += 1

    result = []

    for value in range(len(counting_arr)):
        if counting_arr[value] != 0:
            # print(value, counting_arr[value])
            for index in range(counting_arr[value]):
                result.append(value)


    print(*result)

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)
