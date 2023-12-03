# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true

no_english_students = input()
english_students_set = set(map(int, input().split(' ')))

no_french_students = input()
french_students_set = set(map(int, input().split(' ')))

english_and_french_only = english_students_set.symmetric_difference(french_students_set)

print(len(english_and_french_only))