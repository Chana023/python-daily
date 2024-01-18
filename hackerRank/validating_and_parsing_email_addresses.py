import re
import email.utils

no_of_numbers = int(input())

for value in range(0, no_of_numbers, 1):
    
    s = input()
    
    email_in_list = list(email.utils.parseaddr(s))

    match = re.search(r'^[A-Za-z0-9]([A-Za-z0-9-_.]+)@[A-Za-z]+\.([A-Za-z]{0,3}$)', email_in_list[1])

    if match:
        print(email.utils.formataddr(email_in_list))
    else:
        pass


