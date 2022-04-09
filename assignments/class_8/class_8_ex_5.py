# 1. Download the file exercise3_shopping.csv from Google Classroom
# 2. Read file exercise3_shopping.csv
# 3. print the items in a formatted, easy to read way
# 4. Calculate and print the amount of items bought
# 5. Calculate and print total amount of money spent

import pathlib
path = pathlib.Path(__file__).parent.resolve() / 'exercise3_shoping.csv'

# create a shopping dictionary
shopping = {}

with open(path) as file:
    # skip first line
    next(file)

    # go through each line
    for line in file.readlines():
        # unpack item, qty and price from comma separated string (line)
        [item, qty, price] = line.strip().split(',')

        # correct datatype
        qty = int(qty)
        price = float(price)

        # add shopping item
        shopping[item] = {'qty': qty, 'price': price}

        # print shopping list (easy to read way)
        print(f'{item}: {shopping[item]}')


def calculate_item_count_and_money_spent(shopping):
    items_count = 0
    money_spent = 0
    for item in shopping.values():
        items_count += item['qty']
        money_spent += item['price'] * item['qty']
    print(f'Items count: {items_count}')
    print(f'money spent: {money_spent:0.2f}')


calculate_item_count_and_money_spent(shopping)
