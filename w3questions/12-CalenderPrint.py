# Write a Python program to print the calendar of a given month and year.

import calendar

print('Input the Month you would like to view:')
month = int(input())
print('Input the year you would like to view:')
year = int(input())

calender1 = calendar.month(year,month)

print(calender1)

