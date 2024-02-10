# https://www.hackerrank.com/challenges/np-array-mathematics/problem

import numpy as np

n, m = input().split(' ')

n = int(n)
m = int(m)

a = []
b = []

row = []
for value in range(n):
    row = input().split(' ')
    a.append(row)
    row = []


for value in range(n):
    row = input().split(' ')
    b.append(row)
    row = []

a = np.array(a, float)
b = np.array(b, float)

print(np.add(a, b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))
print(np.mod(a,b))
print(np.power(a,b))