# https://www.hackerrank.com/challenges/separate-the-numbers/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    h = 1

    if len(s) == 1:
            print('NO')
            return 'NO'

    for value in range(0, (len(s)//2), 1):

        a = s[:h]
        a = int(a)
        new_s = str(a)
        initial = a
        
        while len(new_s) != len(s):
            a = a + 1
            new_s = new_s + str(a)

            if len(new_s) >= len(s):
                break

        if new_s != s:
            new_s = ''
            h += 1

        if new_s == s:
            break

    if new_s == s:
        print('YES', initial)
        return 'YES', initial
        
    else:
        print('NO')
        return 'NO'

        

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
