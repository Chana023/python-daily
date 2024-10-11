# https://www.hackerrank.com/challenges/dynamic-array/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    arr = [[]for i in range(n)]
    lastAnswer = 0
    ansArray = []
    
    for val in queries:
        if val[0] == 1:
            idx = (val[1] ^ lastAnswer) % n
            arr[idx].append(val[2])
        else:
            idx = (val[1] ^ lastAnswer) % n
            i = val[2] % len(arr[idx])
            lastAnswer = arr[idx][i]
            ansArray.append(lastAnswer)
        
    return ansArray

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)
