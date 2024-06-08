# https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def hackerrankInString(s):
    # Write your code here
    keyword = 'hackerrank'
    count = 0
    index = 0

    for value in keyword:

        while index < len(s):

            if value == s[index]:
                count += 1
                index += 1
                break

            index += 1
        
    if count == len(keyword):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

