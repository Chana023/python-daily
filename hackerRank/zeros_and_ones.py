# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true

import numpy

n, m , p = input().split(' ')

n = int(n)
m = int(m)
p = int(p)

for value in range(p):
    print(numpy.zeros((n,m), dtype=int))
    print('\n')

for value in range(p):
    print(numpy.ones((n,m), dtype=int))
    print('\n')