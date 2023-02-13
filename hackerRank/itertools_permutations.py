from itertools import permutations

string, k = input().split(' ')

string_list = list(string)
string_list.sort()

permutations_tuple = permutations(string_list, int(k))

for value in permutations_tuple:
        print(''.join([str(i[0]) for i in value]))