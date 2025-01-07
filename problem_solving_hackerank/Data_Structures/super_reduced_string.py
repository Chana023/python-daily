# https://www.hackerrank.com/challenges/reduced-string/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    x = 0 

    while x < len(s) - 1:
        if s[x] == s[x+1]:
            s = s[:x] + s[x+2:]
            x = 0
        else: 
            x = x + 1

    print(s if s else "Empty String")


if __name__ == '__main__':

    s = input()

    result = superReducedString(s)

