# https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true

elements_in_set = input()

set_A = set(map(int, input().split(' ')))

N = int(input())

for value in range(N):

    operation = list(input().split(' '))
    new_set = set(map(int, input().split(' ')))

    if operation[0] == 'intersection_update':
        set_A.intersection_update(new_set)
    elif operation[0] == 'update':
        set_A.update(new_set)
    elif operation[0] == 'symmetric_difference_update':
        set_A.symmetric_difference_update(new_set)
    elif operation[0] == 'difference_update':
        set_A.difference_update(new_set)
    
    print(set_A)

sum = 0 

for value in set_A:
    sum += value

print(sum)