# https://www.hackerrank.com/challenges/input/problem?isFullScreen=true

x, k = map(int, input().split(' '))
P = input()


if eval(P) == k:
    print('True')
else:
    print('False')