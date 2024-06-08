# https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    freqs = defaultdict(int)
    for n in s:
        freqs[n % k] += 1
    result = min(freqs[0], 1)
    for i in range(1, k//2 +1):
        if i==k-i:
            result+=1
        else:
            result+=max(freqs[i],freqs[k-i])
    return result


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)
