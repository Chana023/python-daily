# https://www.hackerrank.com/challenges/save-the-prisoner/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#

def saveThePrisoner(n, m, s):
    # Write your code here

    count = 1
    start = s
    
    while count != m+1:

        if count == m:
            return s

        print(count, s)

        if s == n:
            s = 1
            count = count + 1
            continue

        s = s + 1

        
        count = count + 1


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)


