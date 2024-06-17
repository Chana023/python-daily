# https://www.hackerrank.com/challenges/making-anagrams/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def makingAnagrams(s1, s2):
    # Write your code here
    count1 = Counter(s1)
    count2 = Counter(s2)
    return (count1-count2).total() + (count2-count1).total()

    


if __name__ == '__main__':

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)


