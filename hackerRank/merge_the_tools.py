def merge_the_tools(string, k):
    # your code goes here
    list_of_substring = [string[i:i + k] for i in range(0, len(string),k)]
    substring_no_duplicates = [] 
    list_of_substring_no_dup = []

    for value in range(0, len(list_of_substring), 1):

        [substring_no_duplicates.append(item) for item in list_of_substring[value] if item not in substring_no_duplicates]
        list_of_substring_no_dup.append(''.join(substring_no_duplicates))



        substring_no_duplicates.clear()
    
    
    [print(i) for i in list_of_substring_no_dup]

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)