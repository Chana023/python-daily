from collections import defaultdict

n, m = input().split(' ')
n = int(n)
m = int(m)

d = defaultdict(list)
group_b = []

for value in range(0,n,1):
    d[value].append(input())

for value in range(0,m,1):
    group_b.append(input())

result_str = ''

for b_index in range(0,len(group_b),1):
    for d_key in range(0,len(d),1):
        if group_b[b_index] == d[d_key][0]:
            result_str = result_str + ''.join(str(d_key+1)) + ' '
    if(result_str != ''):
        print(result_str)
    else:
        print(-1)
    result_str = ''

