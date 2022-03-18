#Write a Python program to accept a filename from the user and print the extension of that.

print('Please input the filename')
filename = input()

extension = filename.split('.')

print(extension[1])