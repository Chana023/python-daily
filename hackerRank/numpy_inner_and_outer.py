# https://www.hackerrank.com/challenges/np-inner-and-outer/problem?isFullScreen=true

import numpy

a = input().split(' ')
b = input().split(' ')
    
a = numpy.array(a, int)
b = numpy.array(b, int)

print(numpy.inner(a,b))
print(numpy.outer(a,b))