def print_rangoli(size):
    max_letter = 96 + size

    width = (4*size) - 3
    length = (2*size) - 1
    all_letters = []

    for letter in range(max_letter, 96, -1):
        all_letters.append(chr(letter))

    

    # Top pyramid



    # Middle row generation 
    middle_row = []
    all_letters_minus_first = all_letters.copy()
    all_letters_minus_first.reverse()
    all_letters_minus_first.pop(0)


    middle_row = all_letters + all_letters_minus_first

    middle_row_value = '-'.join(middle_row)
    

    print(middle_row_value)

    # Bottom pyramid
        

        

    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)