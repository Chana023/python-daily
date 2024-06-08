# https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here

    count_Array = []
    pair_count = 0

    for value in ar:
        count = ar.count(value)
        count_Array.append((value,count))
    
    set_Array = set(count_Array)

    for value in set_Array:
        pair_count = pair_count + (value[1] // 2)

    print(pair_count)
        

if __name__ == '__main__':

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

