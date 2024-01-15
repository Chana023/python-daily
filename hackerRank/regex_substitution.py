# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem?isFullScreen=true
import re

n = int(input())

result = []

for line in range(0, n, 1):
    x = input()

    x = re.sub(r"(?<=\s)(&&)(?=\s)", r'and', x)
    x = re.sub(r"(?<=\s)(\|\|)(?=\s)", r'or', x)

    result.append(x)

print('\n'.join(result))