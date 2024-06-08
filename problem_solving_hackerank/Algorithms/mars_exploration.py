# https://www.hackerrank.com/challenges/mars-exploration/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    count = 0
    message = 'SOS'
    length = len(s)
    mult = length / 3
    message = message * int(mult)
    

    for value in range(len(message)):
        if message[value] != s[value]:
            count += 1


    print(count)

if __name__ == '__main__':

    s = input()

    result = marsExploration(s)

