# https://www.hackerrank.com/challenges/extra-long-factorials/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    fact = 1

    for value in range(1, n+1):
        fact = fact * value

    return fact

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
