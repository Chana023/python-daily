# https://www.hackerrank.com/challenges/np-concatenate/problem?isFullScreen=true

import numpy

n, m, p = input().split(' ')

n = int(n)
m = int(m)
p = int(p)

matrix_1 = []
matrix_2 = []

for value in range(n):
    row = input().split(' ')
    matrix_1.append(row)

    row = []

matrix_1 = numpy.array(matrix_, int)


for value1 in range(m):
    row = input().split(' ')
    matrix_2.append(row)

    row = []

matrix_2 = numpy.array(matrix_2, int)

print(numpy.concatenate((matrix_1, matrix_2), axis=0))

