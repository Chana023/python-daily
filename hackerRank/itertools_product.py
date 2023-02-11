A = list(input().split(' '))
B = list(input().split(' '))

result = []
result_string = ''

for value in range(0, len(A), 1):
    for value2 in range(0, len(B), 1):
        result.append((int(A[value]), int(B[value2])))

for value in range(0, len(result), 1):
    result_string = result_string + str(result[value]) + ' '

print(result_string)