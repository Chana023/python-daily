# https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true

no_english_students = input()
english_students_set = set(map(int, input().split(' ')))

no_french_students = input()
french_students_set = set(map(int, input().split(' ')))

only_english = english_students_set.difference(french_students_set)

print(len(only_english))

