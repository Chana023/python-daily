# https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true

number_of_cases = int(input())

for value in range(number_of_cases):
    input()
    set_A = set(input().split())
    input()
    set_B = set(input().split())

    if set_A.issubset(set_B):
        print('True')
    else:
        print('False')
