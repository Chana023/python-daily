import textwrap

def wrap(string, max_width):
    result = textwrap.wrap(string, max_width)
    resultstr = ''
    for x in result:
        resultstr = resultstr + str(x) + '\n'
    return resultstr

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)