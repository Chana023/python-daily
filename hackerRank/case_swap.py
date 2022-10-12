
def swap_case(s):
    case_swap_str = ''
    for index in range(len(s)):
        if s[index].islower():
            case_swap_str = case_swap_str + s[index].upper()
        elif s[index].isupper():
            case_swap_str = case_swap_str + s[index].lower()
        else:
            case_swap_str = case_swap_str + s[index].lower()
    return case_swap_str

    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)

    print(result)