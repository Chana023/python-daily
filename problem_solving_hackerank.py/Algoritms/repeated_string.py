# https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    count = 0
    for value in s:
        if value == 'a':
            count = count + 1

    count = count * (n // len(s))

    remainder = n % len(s)

    split_s = s[:remainder]

    for value in split_s:
        if value == 'a':
            count = count + 1

    print(count)
    

if __name__ == '__main__':
    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)


