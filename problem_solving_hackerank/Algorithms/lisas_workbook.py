# https://www.hackerrank.com/challenges/lisa-workbook/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    # Write your code here
    page_no = 1
    problem_count = 0
    special_problem_count = 0

    for chapter in arr:
        if problem_count != 0:
            problem_count = 0
            page_no = page_no + 1
        
        for value in range(1, chapter+1, 1):
            
            if page_no == value:
                special_problem_count = special_problem_count + 1


            problem_count = problem_count + 1
            
            if problem_count == k:
                page_no = page_no + 1
                problem_count = 0

    print(special_problem_count)

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

