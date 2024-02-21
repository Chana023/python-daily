# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    count_max = 0
    count_min = 0
    current_max = scores[0]
    current_min = scores[0]

    for value in scores:
        if value > current_max:
            count_max = count_max + 1
            current_max = value
        elif value < current_min:
            count_min = count_min + 1
            current_min = value

    print(count_max, count_min)


if __name__ == '__main__':
    

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    
