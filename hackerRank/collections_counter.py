#  is a shoe shop owner. His shop has number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are number of customers who are willing to pay

# amount of money only if they get the shoe of their desired size.

# Your task is to compute how much money

# earned.

# Input Format

# The first line contains
# , the number of shoes.
# The second line contains the space separated list of all the shoe sizes in the shop.
# The third line contains , the number of customers.
# The next lines contain the space separated values of the desired by the customer and , the price of the shoe.

from collections import Counter

number_of_shoes = input()
list_of_shoes = list(input().split(' '))
list_of_shoes = [int(i) for i in list_of_shoes]
number_of_cutomers = int(input())

counter = 1
income = 0
while counter <= number_of_cutomers:
    size, price = input().split(' ')

    if int(size) in list_of_shoes:
        list_of_shoes.remove(int(size))
        income = income + int(price)

    counter = counter + 1

print(income)