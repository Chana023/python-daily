#Write a Python program to get a string which is n (non-negative integer) copies of a given string.

print('Enter a string you need duplicated')
string = input()
print('Enter the number of times you need the string duplicated?')
n = int(input())

result = ''

for num in range(n):
    result = result + string

print(result)