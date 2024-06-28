# https://www.hackerrank.com/challenges/marcs-cakewalk/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#

def marcsCakewalk(calorie):
    # Write your code here
    calorie.sort(reverse=True)

    sum = 0

    for value in range(len(calorie)):
        sum = sum + (calorie[value] * pow(2, value))

    print(sum)

if __name__ == '__main__':

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)
