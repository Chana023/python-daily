# https://www.hackerrank.com/challenges/sherlock-and-squares/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Write your code here
    start_square = int(a ** 0.5)
    end_square = int(b ** 0.5)

    count = end_square - start_square + 1 if start_square ** 2 == a else end_square - start_square

    return count

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        
