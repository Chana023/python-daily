# https://www.hackerrank.com/challenges/python-sort-sort/problem?isFullScreen=true

import math
import os
import random
import re
import sys
import operator



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    result = []

    result = sorted(arr, key=operator.itemgetter(k))

    for value in result:
        print(*value, end="\n")
