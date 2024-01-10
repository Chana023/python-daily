# https://www.hackerrank.com/challenges/re-group-groups/problem?isFullScreen=true

import re

s = str(input())

m = re.search(r'([a-zA-Z0-9])(\1+)' , s)

if m:
    print(m.group(1))
else:
    print('-1')