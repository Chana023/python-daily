# https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#


def biggerIsGreater(w):
    # Write your code here

    pivot_index = 0
    break_bool = False
    count = 0
    for value in range(len(w) -1, -1, -1):
        if w[value -1] < w[value]:
            pivot_index = value -1
            count = value
            break
        # print(value)

    if count == 0:
        print('no answer')
        return
        
    pivot = w[pivot_index]

    for value in range(len(w) -1, -1, -1):
        if pivot < w[value]:
            swap_char_index = value
            break

    char_list = list(w)
    char_list[pivot_index], char_list[swap_char_index]  = char_list[swap_char_index], char_list[pivot_index]
    
    suffix_list = char_list[pivot_index + 1:]
    suffix_list.reverse()
    char_list = char_list[0:pivot_index + 1] + suffix_list

    w = ''.join(char_list)

    print(w)

    

            



if __name__ == '__main__':

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

