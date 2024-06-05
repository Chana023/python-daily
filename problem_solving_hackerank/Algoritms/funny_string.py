# https://www.hackerrank.com/challenges/funny-string/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    s_ascii = [ ord(x) for x in s ]
    s_ascii_reverse = s_ascii[::-1]

    res_1 = []
    res_2 = []

    for value in range(1, len(s_ascii), 1):
        res_1.append(abs( s_ascii[value-1] - s_ascii[value]))
        res_2.append(abs( s_ascii_reverse[value-1] - s_ascii_reverse[value]))

    if res_1 == res_2:
        print('Funny')
    else:
        print('Not Funny')

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

