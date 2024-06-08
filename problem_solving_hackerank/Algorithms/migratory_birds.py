# https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    set_of_input = set(arr)

    result_list = []

    for value in set_of_input:
        result_list.append((value ,arr.count(value)))

    max_tuple = max(result_list, key=lambda tup: tup[1])

    print(max_tuple[0])


        

if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

