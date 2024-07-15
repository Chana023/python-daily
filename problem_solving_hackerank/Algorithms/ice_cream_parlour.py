# https://www.hackerrank.com/challenges/icecream-parlor/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    # Write your code here
    print(m, arr)

    for value in range(len(arr)):
        for index in range(value+ 1,len(arr)):
            if arr[value] + arr[index] == m:
                result = []
                result.append(value + 1)
                result.append(index + 1)
                print(*result)
                return 

    


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

