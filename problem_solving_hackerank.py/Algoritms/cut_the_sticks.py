# https://www.hackerrank.com/challenges/cut-the-sticks/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    print(len(arr))    

    while arr:

        shortest_stick = min(arr)
        arr = [x - shortest_stick for x in arr]
        arr = [y for y in arr if y != 0 ]
        if len(arr) != 0:
            print(len(arr))
        

        

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    
