# https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true

import numpy

n, m = input().split(' ')

n = int(n)
m = int(m)

matrix_1 = []

for value in range(n):
    row = input().split(' ')
    matrix_1.append(row)

    row = []

matrix = numpy.array(matrix_1, int)

result = numpy.min(matrix, axis=1)
print(numpy.max(result))