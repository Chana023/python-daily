
def solve(s):
    new_string = []
    s = str(s).split()

    for value in s:
        new_string.append(value.capitalize())

    s = ' '.join(new_string)

    return s

if __name__ == '__main__':

    s = input()

    result = solve(s)

    print (result)