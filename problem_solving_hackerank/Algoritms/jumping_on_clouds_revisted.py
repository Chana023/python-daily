# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    
    energy_level = 100
    k = k if n % k == 0 else math.gcd(n, k)

    for value in range(0, len(c) , k):
        
        
        energy_level = energy_level - 1
        if c[value] == 1:
            energy_level = energy_level - 2
            

        print(energy_level)






if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)
