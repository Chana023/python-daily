# https://www.hackerrank.com/challenges/mark-and-toys/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    # Write your code here
    prices = list(prices)
    prices.sort()

    print(prices)

    counter = 0
    sum = 0

    for index in range(0, len(prices),1):
        sum = sum + prices[index]
        if sum <= k:
            counter += 1
        if sum > k:
            break
    
    print(counter)

        

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)