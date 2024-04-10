# https://www.hackerrank.com/challenges/halloween-sale/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#

def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    total = 0
    current_price = 0
    counter = 0
    while s >= total + current_price and s > p :

        if p < m:
            total = total + m
            current_price = m
        else:
            total = total + p 
            current_price = p

        counter = counter + 1
        p = p - d


    print(counter)
        


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    
