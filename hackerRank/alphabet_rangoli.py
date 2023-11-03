def print_rangoli(size):
    max_letter = 96 + size

    width = (4*size) - 3
    length = (2*size) - 1
    all_letters = []
    final_string = ''

    for letter in range(max_letter, 96, -1):
        all_letters.append(chr(letter))

    
    # Top pyramid
    line_list = []
    reverse_line_list = []
    bottom_lines  =[]
    for x in range(0,size-1,1):
        line_list = all_letters[0:x+1]

        reverse_line_list = line_list.copy()
        reverse_line_list.reverse()
        reverse_line_list.pop(0)

        line_list = line_list + reverse_line_list

        line = '-'.join(line_list)
        line = line.center(width,'-')

        bottom_lines.append(line)
        final_string = final_string + line + '\n'


    # Middle row generation 
    middle_row = []
    all_letters_minus_first = all_letters.copy()
    all_letters_minus_first.reverse()
    all_letters_minus_first.pop(0)

    middle_row = all_letters + all_letters_minus_first
    middle_row_value = '-'.join(middle_row)  
    
    final_string = final_string + middle_row_value + '\n'

    

    # Bottom pyramid
    bottom_lines.reverse()

    for y in range(0,size-1,1):
        final_string = final_string + bottom_lines[y] + '\n'

    return final_string


        

    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)