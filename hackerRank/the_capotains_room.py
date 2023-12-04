# https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true

group_size = int(input())
list_of_room_numbers = list(map(int, input().split(' ')))

rooms_assigned = set(list_of_room_numbers)
value_count = 0

for value in rooms_assigned:
    for x in list_of_room_numbers:
        if value == x:
            value_count += 1

    # print(value, value_count)
    if value_count == 1:
        print(value)
        break    
    value_count = 0

