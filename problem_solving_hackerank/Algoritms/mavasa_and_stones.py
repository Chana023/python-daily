# https://www.hackerrank.com/challenges/manasa-and-stones/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b
#

def stones(n, a, b):
    # Write your code here
    sum_numbers = []
    i = n-1
    j = 0
    while i>=0:
        sum_numbers.append(a*i + b*j)
        i -=1
        j +=1
    
    return sorted(set(sum_numbers))

if __name__ == '__main__':

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)

        
