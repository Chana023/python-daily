# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=true

import re

pattern = '(?<=[^aeiou\s\d\W_])([aeiou]{2,})(?=[^aeiou\s\d\W_])'
lst = re.findall(rf'{pattern}', input(), re.IGNORECASE)
if lst:
    print(*lst, sep='\n')
else:
    print(-1)