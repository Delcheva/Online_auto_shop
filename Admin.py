
import pandas as pd
import matplotlib.pyplot as plt
from Parts import *


def admin_login_window():
    print(f" Welcome to your profile! ")
    print(f" Enter your ADMIN username: ")
    adm_input_name = str(input()).upper()
    print(" Enter your ADMIN Password: ")
    adm_input_pas = str(input())
    with open("admin.csv", 'r') as adm_file:
        data_reader = csv.reader(adm_file, delimiter=',')
        details = [row for row in adm_file if adm_input_pas in row and adm_input_name in row]
        if not details:
            print("Wrong credentials. Please try again")
            admin_login_window()
        else:
            print(f"Welcome {adm_input_name}")
    admin_window()
    adm_options()


def admin_window():
    print("=====================")
    print("1.Display Menu - A")
    print("2.Add Product - B")
    print("3.User changes - C")
    print("4.Total Income - D")
    print("5.Logout - E")
    print("=====================")


def adm_options():
    admin_input = input(str("Enter your choice: ")).upper()
    if admin_input == "A":
        print("==============================")
        admin_display()
        admin_window()
        adm_options()
    elif admin_input == "B":
        adding_parts()
        print("==============================")
        print("=======New item added.========")
        admin_window()
        adm_options()
    elif admin_input == "C":
        user_changes()
        print("==============================")
        admin_login_window()
        print("==============================")
        adm_options()
    elif admin_input == "D":
        total_income()
        admin_window()
        adm_options()
    elif admin_input == "E":
        logout_window()
    else:
        print("Invalid choice. Please enter valid option!")
        print("==============================")


def admin_display():
    print("Id\tName\tCategory\tCompatible Models-Year\tPrice\tOriginal Price")


def adding_parts():
    n = int(input("Enter the number of items need to be added : "))
    for i in range(n):
        new_id = int(input("Enter id : "))
        new_name = input("Enter Name : ")
        new_category = input("Enter Category : ")
        new_compatible = str(input("Enter models of vehicles Compatible - Year : "))
        new_price = int(input("Enter Price : "))
        new_original = int(input("Enter the original price : "))
        new_available = int(input("Enter Available : "))
        new_items = [new_id, new_name, new_category, new_compatible, new_available, new_price, new_original]
        with open("parts.csv", 'a') as p:
            writer2 = csv.writer(p)
            writer2.writerow(new_items)
            p.close()
        admin_display()


def total_income():
    df2 = pd.read_csv("basket.csv")
    sum1 = df2['Price'].sum()
    print("Your total income is ", sum1)
    sum2 = df2['Price'].value_counts()
    plt.plot(sum2)
    plt.savefig("income.png")
    plt.show()


def logout_window():
    print(f"See you next time.")
    exit()


def user_changes():
    print("=====================")
    print(f"Please choose an option:")
    print("1.Changing Users' first name")
    print("2.Changing Users' last name")
    print("3.Changing Users' email")
    print("4.Changing Users' phone")
    print("5.See the Data Base with clients")
    print("6.Return")
    print("=====================")
    admin_input = str(input())
    if admin_input == "1":
        changing_users_first_name()
    elif admin_input == "2":
        changing_users_last_name()
    elif admin_input == "3":
        changing_users_email()
    elif admin_input == "4":
        changing_users_phone()
    elif admin_input == "5":
        see_all_clients()
    elif admin_input == "6":
        admin_window()
    else:
        print("Wrong choice. Please try again")
        user_changes()


def changing_users_first_name():
    print(f'Please enter email of user you want to change data: ')
    admin_input = str(input()).upper()
    print(f"First Name, Last Name, Email, Phone Number, Date registered")
    change = open("users.csv", 'r')
    data = csv.reader(change, delimiter=',')
    count = 0
    for row in data:
        if row[3] == admin_input:
            print(*row[1:])
            count += 1
        elif count > 2:
            break
    df = pd.read_csv("users.csv")
    original_name = str(input("Enter First Name you want to change: ")).upper()
    new_name = str(input("Enter NEW First Name: ")).upper()
    df["First Name"] = df["First Name"].replace(to_replace={original_name},
                                                value={new_name})
    df.to_csv("users.csv", index=False)
    change.close()
    print("======= Correction successful =======")
    user_changes()


def changing_users_last_name():
    print(f'Please enter email of user you want to change data: ')
    admin_input = str(input()).upper()
    print(f"First Name, Last Name, Email, Phone Number, Date registered")
    with open("users.csv", 'r') as change:
        data = csv.reader(change, delimiter=',')
        count = 0
        for row in data:
            if row[3] == admin_input:
                print(*row[1:])
                count += 1
    df = pd.read_csv("users.csv")
    original_name = str(input("Enter Last Name you want to change: ")).upper()
    new_name = str(input("Enter NEW Last Name: ")).upper()
    df["Last Name"] = df["Last Name"].replace(to_replace={original_name},
                                              value={new_name})
    df.to_csv("users.csv", index=False)
    print("======= Correction successful =======")
    user_changes()


def changing_users_email():
    print(f'Please enter email of user you want to change data: ')
    admin_input = str(input()).upper()
    print(f"First Name, Last Name, Email, Phone Number, Date registered")
    with open("users.csv", 'r') as change:
        data = csv.reader(change, delimiter=',')
        count = 0
        for row in data:
            if row[3] == admin_input:
                print(*row[1:])
                count += 1
    df = pd.read_csv("users.csv")
    original_name = str(input("Enter Email you want to change: ")).upper()
    new_name = str(input("Enter NEW Email: ")).upper()
    df["Email"] = df["Email"].replace(to_replace={original_name},
                                      value={new_name})
    df.to_csv("users.csv", index=False)
    print("======= Correction successful =======")
    user_changes()


def changing_users_phone():
    print(f'Please enter email of user you want to change data: ')
    admin_input = str(input()).upper()
    print(f"First Name, Last Name, Email, Phone Number, Date registered")
    with open("users.csv", 'r') as change:
        data = csv.reader(change, delimiter=',')
        count = 0
        for row in data:
            if row[3] == admin_input:
                print(*row[1:])
                count += 1
    df = pd.read_csv("users.csv")
    original_name = str(input("Enter Phone you want to change: ")).upper()
    new_name = str(input("Enter NEW Phone: ")).upper()
    df["Phone"] = df["Phone"].replace(to_replace={original_name},
                                      value={new_name})
    df.to_csv("users.csv", index=False)
    print("======= Correction successful =======")
    user_changes()


def see_all_clients():
    with open("users.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            print(line[1:])
