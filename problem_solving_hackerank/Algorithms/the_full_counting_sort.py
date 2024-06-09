# https://www.hackerrank.com/challenges/countingsort4/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    max_value = 0
    for value in range(0, int(len(arr)/2),1):
        arr[value][1] = '-'
        if int(arr[value][0]) > max_value:
            max_value = int(arr[value][0])

    result = [[] for _ in range(max_value+1)]

    for value in arr:
        for index in range(len(result)):
            if int(value[0]) == index:
                result[index].append(value[1])

    final_res = ''
    for value in result:
        for index in value:
            final_res = final_res + index + ' '
        

    print(final_res)


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
