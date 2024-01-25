# https://www.hackerrank.com/challenges/validating-uid/problem?isFullScreen=true

import re

no_of_numbers = int(input())

for value in range(0, no_of_numbers, 1):
    
    s = input()
    match = re.search(r'^(?!.*(.).*\1)(?=.*[A-Z].*[A-Z])(?=.*\d.*\d.*\d)[A-Za-z0-9]{10}$', s)

    if match and len(s) == 10:
        print('Valid')
    else:
        print('Invalid')