if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    my_list = []
    for value in arr:
        my_list.append(value)

    my_list.sort(reverse=True)

    for number in my_list:
        if number != my_list[0]:
            print(number)
            break
    