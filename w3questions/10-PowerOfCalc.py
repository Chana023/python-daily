# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

print('Type a value to calulate the value of n+nn+nnn')
value = input()

#result = value + (value**2) + (value**3)

result = int(value) + int(value+value) + int(value+value+value)

print(result)