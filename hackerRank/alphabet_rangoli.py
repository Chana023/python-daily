def print_rangoli(size):
    max_letter = 96 + size

    width = (4*size) - 3
    length = (2*size) - 1
    line_string = '*'

    for row in range(0,length,1):
        for column in range(0,width,1):
            print(str(row) + ' ' + str(column))

        #print(line_string.center(width,'-'))

    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)