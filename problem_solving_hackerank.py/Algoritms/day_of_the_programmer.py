# https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def isLeap(year):
    if year < 1918:
        return year % 4 == 0
    else:
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def dayOfProgrammer(year):
    # Write your code here
    numDaysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    daysCounter = 0
    prevDaysCounter = 0
    leap = isLeap(year)
    target = 256
    if leap:
        numDaysInMonth[1] = 29
    if year == 1918:
        target+=13
    for i in range(0, len(numDaysInMonth)):
        prevDaysCounter = daysCounter
        daysCounter+=numDaysInMonth[i]
        if daysCounter > target:
            days = target - prevDaysCounter
            return f'{days:02}.{i + 1:02}.{year}'
        elif daysCounter == target:
            return f'01.{i + 1}.{year}'

if __name__ == '__main__':

    year = int(input().strip())

    result = dayOfProgrammer(year)

    
