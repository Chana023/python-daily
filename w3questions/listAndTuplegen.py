#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a 
# list and a tuple with those numbers


print("Please provide a list of values which you would like added to a list and tuple:")

list1 = []
tuple1 = ()
notifier = ''

while(notifier != 'end'):
    value = input()
    if(value.isdigit()):
        list1.append(value)

    notifier = value
    
tuple1 = tuple(list1)

print(list1)
print(tuple1)