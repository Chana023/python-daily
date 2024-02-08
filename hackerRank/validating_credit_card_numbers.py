# https://www.hackerrank.com/challenges/validating-credit-card-number/problem?isFullScreen=true

import re

no_of_numbers = int(input())

for value in range(0, no_of_numbers, 1):
    
    s = input()
    match = re.search(r'^(?!.*(\d)(-*\1){3,})([456][0-9]{3}-?([0-9]{4}-?){3})$', s)

    if match:
        print('Valid')
    else:
        print('Invalid')