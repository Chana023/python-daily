# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem?isFullScreen=true

import numpy

input_array = input().split(' ')

matrix = numpy.array(input_array, float)

print(numpy.floor(matrix))
print(numpy.ceil(matrix))
print(numpy.rint(matrix))

