from itertools import combinations

input_string, k = input().split()

k = int(k)

input_string = sorted(input_string)
result_list = []

for value in range(1, k+1,1):
    combinations_list = list(combinations(input_string, value))
    result_list = result_list + combinations_list
    combinations_list = []


for value in result_list:
        print(''.join([i[0] for i in value]))