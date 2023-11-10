# There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

# Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.

# https://www.hackerrank.com/challenges/no-idea/problem

n, m = input().split(' ')

input_list = list(map(int, input().split()))
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))


happiness = 0 

for value in range(0, len(list_A) , 1):
    if list_A[value] in input_list:
        happiness += 1

for value in range(0, len(list_B) , 1):
    if list_B[value] in input_list:
        happiness -= 1

print(happiness)