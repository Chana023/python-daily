# https://www.hackerrank.com/challenges/swap-nodes-algo/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

def swapNodes(indexes, queries):
    # Write your code here
    # Write your code here
    result = []
    indexes = [[]]+indexes
    for k in queries:
        res = []
        swap(indexes, 0, 1, k, res)
        result.append(res)
    return result

def swap(nodes, depth, curr, k, result):
    if curr == -1: 
        return
    if depth % k == k - 1:
        nodes[curr][0], nodes[curr][1] = nodes[curr][1], nodes[curr][0]
    swap(nodes, depth + 1, nodes[curr][0], k, result)
    result.append(curr)
    swap(nodes, depth + 1, nodes[curr][1], k, result)

if __name__ == '__main__':

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)
