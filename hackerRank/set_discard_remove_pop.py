n = int(input())
s = set(map(int, input().split()))

command_number = int(input())

for value in range(command_number):
    command, *value = input().split()
    if value:
        value = int(value[0])
    if command == 'pop':
        s.pop()
    elif command == 'remove':
        s.remove(value)
    elif command == 'discard':
        s.discard(value)

s = [int(i) for i in s]

sum = 0

for number in s:
    sum = sum + number

print(sum)