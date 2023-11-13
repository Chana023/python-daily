# https://www.hackerrank.com/challenges/compress-the-string/problem

import itertools 

input_string = input()

input_list = list(input_string)

answer_string = ''

for key, group in itertools.groupby(input_list):
    answer_string = answer_string + f'({len(list(group))}, {key})' + ' '

print(answer_string)