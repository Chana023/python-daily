# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=true

import numpy

n, m = input().split(' ')

n = int(n)
m = int(m)

matrix_1 = []

for value in range(n):
    row = input().split(' ')
    matrix_1.append(row)

    row = []

matrix = numpy.array(matrix_1, float)

print(numpy.mean(matrix, axis=1))
print(numpy.var(matrix, axis=0))
print(numpy.std(matrix, axis=None))