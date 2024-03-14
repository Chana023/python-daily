# https://www.hackerrank.com/challenges/append-and-delete/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    common_length = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            common_length += 1
        else:
            break

    total_operations = len(s) + len(t) - 2 * common_length
    
    if k >= len(s) + len(t) or (k >= total_operations and (k - total_operations) % 2 == 0):
        print('Yes')
    else:
        print('No')
        

if __name__ == '__main__':

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)
