# https://www.hackerrank.com/challenges/strange-code/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

def strangeCounter(t):
    # Write your code here
    init = 3
    while t > init:
        t = t - init
        init = init * 2

    print(init - t + 1)
        

if __name__ == '__main__':

    t = int(input().strip())

    result = strangeCounter(t)

