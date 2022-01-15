from Parts import main_selections_of_parts
from orders import *


def user_window():
    print("=====================")
    print("1.Display Menu")
    print("2.View all Categories")
    print("3.View all items in Stock and adding to cart")
    print("4.Shopping history")
    print("5.Logout")
    print("======================")
    print("Please choose one from the sections :")
    user_input = str(input())
    if user_input == "1":
        user_window()
    elif user_input == "2":
        main_selections_of_parts()
    elif user_input == "3":
        display_stock()
    elif user_input == "4":
        shopping_history()
    elif user_input == "5":
        log_out()
    else:
        print("Please choose a valid option")
        user_window()


def log_out():
    print(f"See you next time!")
    exit()


class Orders:
    def __init__(self, orders):
        self.orders = orders


def shopping_history():
    print("Welcome to your Order History! ")
    print("Please enter your email: ")
    user_input = str(input()).upper()
    print(f"Username, Items - ID, Date, Cost")
    with open("basket.csv", 'r') as file5:
        data_reader = csv.reader(file5)
        count = 0
        for row in data_reader:
            if row[0] == user_input:
                print(*row[0:])
                count += 1
            elif count > 2:
                break
    user_window()
