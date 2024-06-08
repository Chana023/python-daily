# https://www.hackerrank.com/challenges/permutation-equation/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Write your code here
    index_array = []
    result_array = []
    for value in range(1, len(p) + 1, 1):
        index_array.append(p.index(value) + 1)

    for y in index_array:
        print(p.index(y)+1)


if __name__ == '__main__':

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    
