# https://www.hackerrank.com/challenges/np-sum-and-prod/problem

import numpy

n, m = input().split(' ')

n = int(n)
m = int(m)

row = []
matrix = []
for value in range(n):
    row = input().split(' ')
    matrix.append(row)

    row = []

matrix_a = numpy.array(matrix, int)

result = numpy.sum(matrix_a, axis=0)

print(numpy.prod(result))