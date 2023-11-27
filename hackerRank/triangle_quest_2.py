# You are given a positive integer .
# Your task is to print a palindromic triangle of size .

# You can't take more than two lines. The first line (a for-statement) is already written for you.
# You have to complete the code using exactly one print statement.





for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(*list(range(1 , i + 1)),*list(range(i - 1 , 0, -1)),sep='')