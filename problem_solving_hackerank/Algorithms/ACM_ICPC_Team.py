# https://www.hackerrank.com/challenges/acm-icpc-team/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

from itertools import combinations

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here
    comb = combinations(topic, 2)
    current_max = 0
    max_count = 0

    for i in comb:

        result = bin(int(i[0], 2) | int(i[1], 2))
        # print(i, result, result.count("1"))
        number_of_known_subjects = int(result.count("1"))

        if number_of_known_subjects > current_max:
            current_max = number_of_known_subjects
            max_count = 0

        if number_of_known_subjects == current_max:
            max_count += 1
        
    print(current_max, max_count)

        
    

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)