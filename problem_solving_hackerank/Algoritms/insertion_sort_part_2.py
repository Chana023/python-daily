# https://www.hackerrank.com/challenges/insertionsort2/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    for index in range(1, len(arr)):

        key = arr[index]
        inner_index = index-1 
        while inner_index >= 0 and key < arr[inner_index] :
                arr[inner_index + 1] = arr[inner_index]
                inner_index -= 1
        arr[inner_index + 1] = key

        print(*arr)
            
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
