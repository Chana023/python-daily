# https://s3.amazonaws.com/hr-challenge-images/9668/1440151155-10b2b748ee-rsz_1438840048-2cf71ed69d-findangle.png
# https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true

import math

AB = int(input())
BC = int(input())

result = round(math.degrees(math.atan2((AB/2),(BC/2))))

deg = '\xb0'

print(result,deg,sep="")
