from itertools import combinations_with_replacement

input_string, k = input().split(' ')

input_string = sorted(input_string)
k = int(k)

comb = list(combinations_with_replacement(input_string, k))

for value in comb:
    print(''.join([i[0] for i in value]))