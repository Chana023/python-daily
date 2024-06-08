# https://www.hackerrank.com/challenges/library-fine/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    return_due = datetime.datetime(y2, m2, d2)
    return_date = datetime.datetime(y1, m1, d1)

    if return_date <= return_due:
        print(0)
    elif return_date.day > return_due.day and return_date.month == return_due.month and return_date.year == return_due.year:
        print(15 * (return_date.day - return_due.day))
    elif return_date.month > return_due.month and return_date.year == return_due.year:
        print(500 * (return_date.month - return_due.month))
    elif return_date.year > return_due.year:
        print(10000)

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)


