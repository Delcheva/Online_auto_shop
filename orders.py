import csv
from datetime import datetime

shopping_list = []
prices = {}
stock = {}

with open('parts.csv', 'r') as file:
    reader = csv.DictReader(file)
    prices = {row["ID"]: row["Price"] for row in reader}

with open('parts.csv', 'r') as file:
    reader = csv.DictReader(file)
    item = {row["ID"]: row["Compatible Models-Year"] for row in reader}

with open('parts.csv', 'r') as file:
    reader = csv.DictReader(file)
    stock = {row["ID"]: row["Stock"] for row in reader}


def display_stock():
    print("\nItem ID, Compatible models, Cost")
    print("------------------------------------")
    for key in stock:
        print(key, "\t", item[key], "\t", prices[key])
    fill_cart()


def compute_bill(parts):
    total = 0
    for items in parts:
        if int(stock[items]) > 0:
            total += int(prices[items])
            stock[items] = int(stock[items]) - 1
    return total


def update_data():
    purchase_data = {'user': input('Enter your Email: ').upper(), 'item': shopping_list}
    now = datetime.now()
    purchase_data['date_of_purchase'] = '%s/%s/%s' % (now.day, now.month, now.year)
    purchase_data['cost_of_purchase'] = compute_bill(shopping_list)

    with open('basket.csv', 'a') as file1:
        writer = csv.DictWriter(file1, purchase_data.keys())
        writer.writerow(purchase_data)


def fill_cart():

    i = 0
    while 1:
        i += 1
        part = input("Enter your Item to the List (Press enter to stop): ")
        if part not in stock and part != '':
            print("Item not in Stock")
            part = input("Enter your Item to the List (Press enter to stop): ")
        if part == '':
            break
        shopping_list.append(part)
    update_data()


def display_order():
    print("\nThank you for placing order. Your Order Details are:")
    print("Items, Compatible models, Cost")
    print("--------------------------------")
    for items in shopping_list:
        print(items, "\t", item[items], prices[items])

    bill_cost = compute_bill(shopping_list)
    print("Total Bill Cost: ", bill_cost)




