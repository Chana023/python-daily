# https://www.hackerrank.com/challenges/matrix-script/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded_script = []
column_str = ""

for i in range(m):
    for j in matrix:
        decoded_script.append(j[i])

    column_str = column_str + ''.join(decoded_script)
    decoded_script = []

decoded_script = re.sub(r'(?<=[a-zA-Z0-9])[\s\W_]+(?=[a-zA-Z0-9])', " ", column_str)

print(decoded_script.rstrip())