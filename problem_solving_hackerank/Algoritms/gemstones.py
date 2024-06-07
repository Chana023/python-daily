# https://www.hackerrank.com/challenges/gem-stones/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#

def gemstones(arr):
    # Write your code here
    set_list = []

    for value in arr:
        set_list.append(set(value))

    letter_count = {}

    for value in set_list:
        for index in value:
            if index in letter_count:
                letter_count[index] += 1
            else:
                letter_count[index] = 1

    number_of_rocks = len(arr)
    count = 0


    for value in letter_count:
        if letter_count[value] == number_of_rocks:
            count += 1

    print(count)

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)
