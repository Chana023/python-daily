from collections import deque

operations = int(input())

d = deque()

for action in range(operations):
    command, *value = input().split()

    if value:
        value = int(value[0])

    if command == 'append':
        d.append(value)
    if command == 'appendleft':
        d.appendleft(value)
    if command == 'pop':
        d.pop()
    if command == 'popleft':
        d.popleft()
    

print(' '.join([str(i) for i in d]))