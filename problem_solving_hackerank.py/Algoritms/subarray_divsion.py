# https://www.hackerrank.com/domains/algorithms

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here\
    count_bar = 0
    
    for i in range(len(s) - m + 1):
        sum_bar = 0
        
        for j in range(i, m + i):
            if (m + i < len(s) + 1):
                sum_bar += s[j]
            
        if sum_bar == d:
            count_bar += 1
        
    return count_bar
    

if __name__ == '__main__':


    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

