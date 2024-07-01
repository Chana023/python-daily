# https://www.hackerrank.com/challenges/sherlock-and-array/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    total_sum = sum(arr)
    left_sum = 0

    for value in arr:
        if left_sum == (total_sum - left_sum - value):
            print('YES')
            return 'YES'
        left_sum += value

    return "NO"

if __name__ == '__main__':

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)
