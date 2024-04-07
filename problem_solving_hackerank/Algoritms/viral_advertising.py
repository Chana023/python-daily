# https://www.hackerrank.com/challenges/strange-advertising/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here

    prev_recep = 5
    total_like = 0

    for day in range(1, n+1, 1):

        likes = math.floor(prev_recep/2)
        total_like = total_like + likes
        recepients = math.floor(prev_recep/2) * 3
        

        prev_recep = recepients

    return total_like



if __name__ == '__main__':

    n = int(input().strip())

    result = viralAdvertising(n)

