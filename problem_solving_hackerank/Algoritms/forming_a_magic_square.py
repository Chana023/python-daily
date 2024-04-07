# https://www.hackerrank.com/challenges/magic-square-forming/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def calc_cost(original_value, updated_value):
    return abs(original_value - updated_value)

def formingMagicSquare(s):
    # Write your code here
    possible_solutions = [
        [[4,3,8],[9,5,1],[2,7,6]],
        [[2,9,4],[7,5,3],[6,1,8]],
        [[6,7,2],[1,5,9],[8,3,4]],
        [[8,1,6],[3,5,7],[4,9,2]],
        [[8,3,4],[1,5,9],[6,7,2]],
        [[4,9,2],[3,5,7],[8,1,6]],
        [[2,7,6],[9,5,1],[4,3,8]],
        [[6,1,8],[7,5,3],[2,9,4]]
        ]
    
    cost_list = []
    
    for solution in possible_solutions:
        running_cost = 0
        for row in range(3):
            for value in range(3):
                running_cost = running_cost + calc_cost(s[row][value], solution[row][value])
        
        cost_list.append(running_cost)

    print(min(cost_list))





    

if __name__ == '__main__':


    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

