# https://www.hackerrank.com/challenges/kaprekar-numbers/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here1
    answer = ''
    for value in range(p, q + 1, 1):
        square = value ** 2
        str_square = str(square)

        if square == 1:
            answer = answer + ' ' + str(value)
        elif square > 10:
            left , right = str_square[:len(str_square)//2], str_square[len(str_square)//2:]

            res = int(left) + int(right)

            if res == value:
                answer = answer + ' ' + str(value)
    if answer == '':
        print('INVALID RANGE')
    else:
        print(answer.strip())
        







if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
