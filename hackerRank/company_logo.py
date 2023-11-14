# https://www.hackerrank.com/challenges/most-commons/problem

import itertools
import re

if __name__ == '__main__':
    s = input()

    char_list_count = []

    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1


    sorted_dict = dict(sorted(counts.items(), key=lambda item: (-item[1], item[0])))

    count = 0
    for key, item in sorted_dict.items():
        if count < 3:
            print(key, item)
            count+=1





