# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

from itertools import combinations

size_of_list = int(input())
char_list = input().split(' ')
k = int(input())

comb = combinations(char_list, k)
comb_list = list(comb)

counter = 0
for value in range(len(comb_list)):
    if 'a' in comb_list[value]:
        counter += 1

print(f'{(counter/len(comb_list)):.4f}')