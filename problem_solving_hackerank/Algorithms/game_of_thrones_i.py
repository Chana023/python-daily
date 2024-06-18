# https://www.hackerrank.com/challenges/game-of-thrones/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    # Write your code here
    result = Counter(s)

    odd_count = 0

    for value in result:
        if result[value] % 2 != 0:
            odd_count += 1
        
        if odd_count == 2:
            print('NO')
            return
        
    print('YES')

    

if __name__ == '__main__':

    s = input()

    result = gameOfThrones(s)
