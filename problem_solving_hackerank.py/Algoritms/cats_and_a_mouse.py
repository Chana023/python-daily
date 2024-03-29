# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    
    diff_a = abs(x - z)
    diff_b = abs(y - z)

    if diff_a < diff_b:
        print('Cat A')
    elif diff_b < diff_a:
        print('Cat B')
    elif diff_a == diff_b:
        print('Mouse C')

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)
