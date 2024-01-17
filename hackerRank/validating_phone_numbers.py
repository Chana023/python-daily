# https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true

import re

no_of_numbers = int(input())

for value in range(0, no_of_numbers, 1):
    
    s = input()
    match = re.search(r'^[789]\d{9}', s)

    if match and len(s) == 10:
        print('YES')
    else:
        print('NO')