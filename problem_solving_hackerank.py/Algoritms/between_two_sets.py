# https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    start=min(sorted(a)) 
    end=max(sorted(b))

    factors=[i for i in range(start,end+1) if all(i%x==0 for x in a)]
    second_factors=[i for i in factors if all(x%i==0 for x in b)]
    print(len(second_factors))

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)
