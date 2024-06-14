# https://www.hackerrank.com/challenges/palindrome-index/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here
    for i in range(len(s)//2):
        if s[i] != s[-(i+1)]:
            newstr = s[:i] + s[i+1:] 
            if newstr[:] == newstr[::-1]:
                return i
            return -(i+1)+len(s)
    return -1
    

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)


