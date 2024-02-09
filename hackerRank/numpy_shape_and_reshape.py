# https://www.hackerrank.com/challenges/np-shape-reshape/problem

import numpy

input_list = list(map(int, input().split()))

print(numpy.reshape(input_list ,(3, 3)))