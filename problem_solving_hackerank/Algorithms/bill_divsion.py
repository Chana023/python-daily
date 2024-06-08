# https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    bill_without_item = []
    bill_without_item = bill

    del bill_without_item[k]
    sum_of_bill_without_item = sum(bill_without_item)

    cost_per_person_fair = sum_of_bill_without_item / 2 

    if b - cost_per_person_fair == 0:
        print('Bon Appetit')
    elif b - cost_per_person_fair != 0:
        print(int(b - cost_per_person_fair))



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
