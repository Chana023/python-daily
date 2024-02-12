# https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true

import numpy

n = int(input())

matrix = []
row = []
for value in range(n):
    row = input().split()
    matrix.append(row)

    row = []

matrix = numpy.array(matrix, float)

print(numpy.linalg.det(matrix))