# https://www.hackerrank.com/challenges/luck-balance/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    # print(k , contests)

    contests = sorted(contests, key=lambda x: (-x[1], -x[0]) )
    
    sum = 0
    count = 0

    # print(contests)

    for value in contests:
        if value[1] == 1 and count < k:
            sum += value[0]
            # print('sum', value[0])
            count += 1
        elif value[1] == 1 and count == k:
            sum -= value[0]
            # print('sub', value[0])
        elif value[1] == 0:
            sum += value[0]
            # print('sum', value[0])

    print(sum)

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)