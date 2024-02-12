# https://www.hackerrank.com/challenges/np-polynomials/problem?isFullScreen=true
import numpy

coefficients = list(map(float, input().split()))
value = int(input())

print(numpy.polyval(coefficients, value))