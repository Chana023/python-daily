# https://www.hackerrank.com/challenges/beautiful-binary-string/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#

def beautifulBinaryString(b):
    # Write your code here
    sub_str = '010'
    b = str(b)

    count = b.count(sub_str)

    print(count)

if __name__ == '__main__':

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)
