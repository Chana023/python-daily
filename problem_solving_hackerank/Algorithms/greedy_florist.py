# https://www.hackerrank.com/challenges/greedy-florist/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):

    c = list(c)
    c.sort(reverse=True)

    cost = 0

    for value in range(0,len(c)):
        cost = cost + (value // k + 1) * c[value]
    
    print(cost)

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)


