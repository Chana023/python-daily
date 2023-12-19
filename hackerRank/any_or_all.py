# https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true

N = input()
numbers = []

numbers = input().split()

print(all([int(i) > 0 for i in numbers]) and any([i[::-1] == i for i in numbers]))