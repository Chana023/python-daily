# https://www.hackerrank.com/challenges/np-dot-and-cross/problem/

import numpy

n = input()

n = int(n)

matrix_1 = []
matrix_2 = []

for value in range(n):
    row = input().split(' ')
    matrix_1.append(row)

    row = []

for value in range(n):
    row = input().split(' ')
    matrix_2.append(row)

    row = []

matrix_1 = numpy.array(matrix_1, int)
matrix_2 = numpy.array(matrix_1, int)

print(numpy.dot(matrix_1, matrix_2))