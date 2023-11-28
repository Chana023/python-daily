# The .intersection() operator returns the intersection of a set and the set of elements in an iterable.
# Sometimes, the & operator is used in place of the .intersection() operator, but it only operates on the set of elements in set.
# The set is immutable to the .intersection() operation (or & operation).

number_of_english = input()
set_of_english = set(input().split(' '))

number_of_french = input()
set_of_french = set(input().split(' '))

set_of_both = set_of_english.intersection(set_of_french)

print(len(set_of_both))