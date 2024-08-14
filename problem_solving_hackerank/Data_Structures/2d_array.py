# https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    # print(arr)

    max_sum = float("-inf")

    for value in range(0,4):
        for index in range(0,4):
            top = arr[value][index] + arr[value][index + 1] + arr[value][index + 2]
            mid = arr[value+1][index+1]
            bottom = arr[value + 2][index] + arr[value + 2][index + 1] + arr[value + 2][index + 2]
            sum = top + mid + bottom

            if sum > max_sum:
                max_sum = sum
    
    print(max_sum)



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)


