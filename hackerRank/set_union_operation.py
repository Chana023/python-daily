#  https://www.hackerrank.com/challenges/py-set-union/problem

number_of_students_english = input()
string_of_english_students_roll_numbers = input()
set_of_english_students_numbers = set(string_of_english_students_roll_numbers.split(' '))

number_of_students_french = input()
string_of_french_students_roll_numbers = input()
set_of_french_students_numbers = set(string_of_french_students_roll_numbers.split(' '))

result_list = set_of_english_students_numbers | set_of_french_students_numbers

print(len(result_list))