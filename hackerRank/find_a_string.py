def count_substring(string, sub_string):
    counter = 0
    for index in range(len(string)):
        
        if index == string.find(sub_string, index, len(string)):
            print(index)
            counter += 1
        else:
            pass
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)