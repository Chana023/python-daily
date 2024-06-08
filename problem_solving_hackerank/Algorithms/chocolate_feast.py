# https://www.hackerrank.com/challenges/chocolate-feast/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#

def chocolateFeast(n, c, m):
    # Write your code here

    total_purchased = n / c 
    total_purchased = int(total_purchased)
    total_eaten = total_purchased

    wrappers = total_eaten

    while wrappers >= m:
        total_eaten = total_eaten + int(wrappers / m)

        wrappers = (wrappers % m) + int(wrappers / m)
        

    print(total_eaten)

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        
