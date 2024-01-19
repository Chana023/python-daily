# https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true

import re
for _ in range(int(input())):
    line = input()
    pattern = re.compile(r'#([a-f0-9]){3,6}(?=[,|;|);])', re.I)
    
    for matches in re.finditer(pattern, line):
        print(matches.string)