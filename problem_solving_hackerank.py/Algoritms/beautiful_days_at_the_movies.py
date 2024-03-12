# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def numReverse(num):
    str_num = str(num)
    str_num = str_num [::-1]
    return int(str_num)

def beautifulDays(i, j, k):
    # Write your code here
    list_of_numbers = []

    for value in range(i,j + 1,1):
        list_of_numbers.append(value)

    count = 0

    for day in list_of_numbers:
        result = (day - numReverse(day)) % k

        if result == 0:
            count = count + 1

    return count
    

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)
