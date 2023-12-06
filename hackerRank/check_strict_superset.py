# https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true

set_A = set(map(int, input().split(' ')))
number_of_sample_sets = int(input())
bool_is_superset = True

for value in range(number_of_sample_sets):
    set_B = set(map(int, input().split(' ')))

    if set_A.issuperset(set_B):
        bool_is_superset = True
    else:
        bool_is_superset = False
        print('False')
        break

if bool_is_superset == True:
    print('True')
