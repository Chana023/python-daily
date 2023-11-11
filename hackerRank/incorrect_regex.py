# https://www.hackerrank.com/challenges/incorrect-regex#

# Odd behaviour here, code works in pypy3 but nut in python 3...

import re

number_of_patterns = int(input())

for value in range(0, number_of_patterns, 1):

    regex_pattern = input()

    try:
        re.compile(regex_pattern)
        print(True)
    except re.error as e:
        print(False)