# https://www.hackerrank.com/challenges/pangrams/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    s = s.lower()
    s = re.sub(r"[^a-zA-Z]","",s)

    s = set(s)
    
    if len(s) == 26:
        print('pangram')
    else:
        print('not pangram')


if __name__ == '__main__':

    s = input()

    result = pangrams(s)

# 