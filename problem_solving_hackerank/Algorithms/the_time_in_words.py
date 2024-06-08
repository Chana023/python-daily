# https://www.hackerrank.com/challenges/the-time-in-words/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#


num2word = {1:"one",
            2:"two",
            3:"three",
            4:"four",
            5:"five",
            6:"six",
            7:"seven",
            8:"eight",
            9:"nine",
            10:"ten",
            11:"eleven",
            12:"twelve",
            13:"thirteen",
            14:"fourteen",
            15:"quarter",
            16:"sixteen",
            17:"seventeen",
            18:"eighteen",
            19:"nineteen",
            20:"twenty",
            30:"half"
            }
def timeInWords(h, m):
    if m == 0:
        return num2word[h] + " o' clock"
    if m == 15:
        return num2word[m] + " past " + num2word[h]
    if m == 30:
        return "half past "+ num2word[h]
    if m == 45:
        return "quarter to "+ num2word[h+1]
    if m == 1:
        return num2word[m] + " minute past " + num2word[h]
    if 1<m<=20:
        return num2word[m] + " minutes past " + num2word[h]
    if 20<m<30:
        return "twenty "+ num2word[m-20] + " minutes past " + num2word[h]
    if 30<m<40:
        return "twenty "+ num2word[40-m] + " minutes to " + num2word[h+1]
    if m>= 40:
        return num2word[60-m] + " minutes to " + num2word[h+1]

if __name__ == '__main__':

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    print(result)

