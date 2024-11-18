# https://www.hackerrank.com/challenges/lonely-integer/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys
import numpy

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    result = 0 

    for num in a: 
        result ^= num

    return result
    

if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)
