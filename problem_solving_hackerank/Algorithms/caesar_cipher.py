# https://www.hackerrank.com/challenges/caesar-cipher-1/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    ascii_s = [ord(char) for char in s]
    
    def shift_letter(k, ascii_value):
        if 97 <= ascii_value <= 122:
            shifted = ((ascii_value - 97 + k) % 26 + 97)
        elif 65 <= ascii_value <= 90:
            shifted = ((ascii_value - 65 + k) % 26 + 65)
        else:
            shifted = ascii_value
        
        return shifted
 
    k = k % 26

    shift_s = [shift_letter(k, x) for x in ascii_s]

    shift_s = ''.join([chr(value) for value in shift_s])

    print(shift_s) 



if __name__ == '__main__':

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

