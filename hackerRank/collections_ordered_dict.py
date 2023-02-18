from collections import OrderedDict

number_of_items = int(input())

sold_dict = OrderedDict()

for item in range(number_of_items):
    item_name, price = input().rsplit(maxsplit=1)
    if item_name in sold_dict:
        sold_dict[f'{item_name}'] = sold_dict[f'{item_name}'] + int(price)
    else:
        sold_dict[f'{item_name}'] = int(price)                                                                                                                   

for value in sold_dict:
    print(value + ' ' + str(sold_dict[value]))