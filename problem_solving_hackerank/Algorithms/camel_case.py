# https://www.hackerrank.com/challenges/camelcase/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    # Write your code here
    count = 1

    for value in s:
        if value.isupper():
            count = count + 1

    print(count)

if __name__ == '__main__':

    s = input()

    result = camelcase(s)

