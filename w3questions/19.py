#Write a Python program to get a new string from a given string where "Is" has been added to the front. 
# If the given string already begins with "Is" then return the string unchanged.

print('Type in a string')
x = input()

if x[0] == 'I' and x[1] == 's':
    print(x)
else:
    print('Is' + x)