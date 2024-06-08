# https://www.hackerrank.com/challenges/alternating-characters/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    # Write your code here
    s = list(s)
    indices_to_pop = []

    for value in range(1, len(s) ,1):
        if s[value] == s[value - 1]:
            indices_to_pop.append(value - 1)

    print(len(indices_to_pop))

        

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

