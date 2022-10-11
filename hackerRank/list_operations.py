""""
Consider a list (list = []). You can perform the following commands:

    insert i e: Insert integer 

at position
.
print: Print the list.
remove e: Delete the first occurrence of integer
.
append e: Insert integer

    at the end of the list.
    sort: Sort the list.
    pop: Pop the last element from the list.
    reverse: Reverse the list.

Initialize your list and read in the value of
followed by lines of commands where each command will be of the types listed above. Iterate through each command in order and perform the corresponding operation on your list. 
"""

if __name__ == '__main__':
    N = int(input())

    list = []

    for _ in range(N):
        x = input().split()
        if x[0] == 'insert':
            list.insert(x[1],x[2])
        elif x[0] == 'print':
            print(list)
        elif x[0] == 'remove':
            list.remove(x[1])
        elif x[0] == 'append':
            list.append(x[1])
        elif x[0] == 'sort':
            list.sort()
        elif x[0] == 'pop':
            list.pop()
        elif x[0] == 'reverse':
            list.reverse()


