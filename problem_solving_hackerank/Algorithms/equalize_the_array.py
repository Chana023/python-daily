# https://www.hackerrank.com/challenges/equality-in-a-array/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Write your code here
    result = Counter(arr)

    sorted_result = sorted(result.items(), key=lambda x:x[1],reverse=True)

    most_common_value = sorted_result[0][0]
    most_common_value = int(most_common_value)

    counter = 0
    for value in arr:
        if value != most_common_value:
            counter = counter + 1

    print(counter)
            
if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)
