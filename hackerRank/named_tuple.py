from collections import namedtuple

number_of_students = input()

student_data = namedtuple('Student', input())

sum = 0

for _ in range(int(number_of_students)):
    s = student_data(*input().split())
    sum += int(s.MARKS)

average = sum / int(number_of_students)
print(average)
