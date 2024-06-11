# https://www.hackerrank.com/challenges/the-love-letter-mystery/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def theLoveLetterMystery(s):
    # Write your code here
    
    total = 0
    for i in range(int(len(s)//2)):
        total += abs(ord(s[i]) - ord(s[-1-i]))
    return total

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

