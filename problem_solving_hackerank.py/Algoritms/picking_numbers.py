# https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here

    maximum = 0
    for value in a:
        c = a.count(value)
        d = a.count(value - 1)
        c = c + d
        
        if c > maximum:
            maximum = c

    print(maximum)
        

        

if __name__ == '__main__':


    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

