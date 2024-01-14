# https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true

import re 

s = input()
k = input()


matches = re.finditer(r'(?=({}))'.format(k), s)
matches_list = list(matches)

if not matches_list:
    print('(-1, -1)')
else:
    for match in matches_list:
        t = (match.start(1), match.end(1)-1)
        print(t)
