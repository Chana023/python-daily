# https://www.hackerrank.com/challenges/find-digits/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    str_n = str(n)
    str_n = list(str_n)

    single_digit_list = [int(x) for x in str_n]

    count = 0

    for value in single_digit_list:
        try:
            if n % value == 0:
                count = count + 1
        except:
            pass

    print(count)

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)


