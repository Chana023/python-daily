# https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true

n = input()

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

for value in range(int(n)):
    input_value = input()

    if input_value == '0':
        print('False')
    else:
        print(is_float(input_value))