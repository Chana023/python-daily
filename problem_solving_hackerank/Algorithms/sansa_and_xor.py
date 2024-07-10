# https://www.hackerrank.com/challenges/sansa-and-xor/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def sansaXor(arr):
    # Write your code here
    if len(arr) == 0: 
        return 0
    
    return getXor(arr)

def getXor(lst):
    ans = 0
    for i in range(0, len(lst), 2):
        ans ^= lst[i]
    return ans

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)
