#Write a Python program to get the difference between 
#a given number and 17, if the number is greater than 17 return double the absolute difference.

print('Please enter a value')
x = int(input())

result = x - 17

if(x > 17 ):
    print(result = abs(result * 2)) 
else:
    print(result)