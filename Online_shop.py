from Users import user_login, user_registration, first_window
from Admin import *
from others import user_window


first_window()
user_input = input()


def logging_in():
    if user_input == "0":
        print(f"Welcome to our registration form ")
        user_registration()
        user_login()
        user_window()
    elif user_input == "1":
        user_login()
        user_window()
    elif user_input == "9":
        print(f"Welcome to Admin Menu")
        admin_login_window()
    else:
        print(f"Wrong choice. Please try again.")
        first_window()


logging_in()





