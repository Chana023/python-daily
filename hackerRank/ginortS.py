# https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true

input_string = str(input())

odd_list = []
even_list = []
is_upper_letter_list = []
is_lower_letter_list = []

def is_even(number_str):
    number = int(number_str)
    if number%2 == 0:
        return True
    else:
        return False

for letter in input_string:
    if letter.isnumeric() and is_even(letter) == True:
        even_list.append(letter)
    elif letter.isnumeric() and is_even(letter) == False:
         odd_list.append(letter)
    elif letter.isupper() == True:
        is_upper_letter_list.append(letter)
    else:
        is_lower_letter_list.append(letter)

even_list = sorted(even_list)
odd_list = sorted(odd_list)
is_upper_letter_list = sorted(is_upper_letter_list)
is_lower_letter_list = sorted(is_lower_letter_list)

result = ''.join(is_lower_letter_list) + ''.join(is_upper_letter_list) + ''.join(odd_list) + ''.join(even_list)


print(result)


