# https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # Write your code here

    sum_of_types = [sum(x) for x in zip(*container)]
    sum_of_container_size = [sum(x) for x in container]

    if sorted(sum_of_types) == sorted(sum_of_container_size):
        print("Possible")
    else:
        print("Impossible")

    
        
    


if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)
