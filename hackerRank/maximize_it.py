# https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true

number_of_lists, m = input().split()

number_of_lists = int(number_of_lists)
list_of_max = []

for l in range(number_of_lists):
    temp_list = []

    temp_list = list(map(int, input().split(' ')))
    list_of_max.append(max(temp_list))

print(list_of_max)


result = 0 

for x in list_of_max:
    result = result + x**2

# result = result % int(m)

print(result)

# Better solution using itertools

# import itertools

# k, m = [int(x) for x in input().split()]
# list_k = []

# for i in range(k):
#     list_k.append(set(map(lambda x: int(x)**2 % m, input().split()[1:])))

# prod = set(sum(x) % m for x in itertools.product(*list_k))
# print(max(prod))