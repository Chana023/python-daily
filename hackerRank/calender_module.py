import calendar

month, day, year = input().split(' ')

day_of_week_int = calendar.weekday(int(year), int(month), int(day))
print((calendar.day_name[day_of_week_int]).upper())

