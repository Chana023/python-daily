# https://www.hackerrank.com/challenges/priyanka-and-toys/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'toys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY w as parameter.
#

def toys(w):
    # Write your code here
    w = list(w)
    w.sort()

    current_min = w[0]
    count = 1

    print(w)

    for value in w:
        if value > current_min + 4:
            count = count + 1
            current_min = value
            print(current_min)

    print(count)

if __name__ == '__main__':

    n = int(input().strip())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)
