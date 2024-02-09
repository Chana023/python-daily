# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy

n, m = input().split(' ')
n = int(n)
m = int(m)

matrix =[]
temp_list = []

for value in range(n):
    row = input().split(' ')

    matrix.append(row)
    
matrix = numpy.array(matrix,int)

print(numpy.transpose(matrix))
print(numpy.array(matrix,int).flatten())
