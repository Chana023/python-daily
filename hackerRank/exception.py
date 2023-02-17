T = input()

T = int(T)

responses_list = []

for value in range(0,T,1):
    a, b = input().split()
    try:
        a = int(a)
        b = int(b)
        responses_list.append(int(a/b))
    except ZeroDivisionError as e:
        responses_list.append('Error Code: integer division or modulo by zero')
    except ValueError as e:
        responses_list.append(f'Error Code: {e}')

for response in responses_list:
    print(response)

