# https://www.hackerrank.com/challenges/fair-rations/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

def fairRations(B):
    # Write your code here
    no_of_breads = 0
    n = len(B)

    for i in range(n-1):
        if B[i]%2 == 1:
            no_of_breads += 2
            B[i+1] += 1

    if B[n-1]%2 == 1:
        print('NO')
    else:
        print(no_of_breads)


if __name__ == '__main__':

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

