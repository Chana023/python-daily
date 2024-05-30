# https://www.hackerrank.com/challenges/strong-password/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = set("0123456789")
    lower_case = set("abcdefghijklmnopqrstuvwxyz")
    upper_case = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    special_characters = set("!@#$%^&*()-+")

    list_pass = set(password)

    char_count = 0

    if not list_pass.intersection(numbers):
        char_count += 1
    elif not list_pass.intersection(lower_case):
        char_count += 1
    elif not list_pass.intersection(upper_case):
        char_count += 1
    elif not list_pass.intersection(special_characters):
        char_count += 1

    min_length = max(0, 6-n)
    print(max(char_count, min_length))





if __name__ == '__main__':

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)


