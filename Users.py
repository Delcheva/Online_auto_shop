from orders import *
from datetime import datetime
from others import user_window


USER_BASE = "users.csv"
new_user = []
check_user = []
user_email = []

with open("users.csv", 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')


header = ['Password', 'First Name', 'Last Name', 'Email', 'Phone', 'Date Registered']


def first_window():
    print(f" Welcome to the new online shop! \n")
    print(f" You will need registration to enter.\n If you don't have please enter 0. \n "
          f"If you already have - please enter 1.\n For ADMIN menu - please enter 9")


class UserId:

    def __init__(self, new_user_fn,
                 new_user_ln, new_user_em,
                 new_user_phone, _new_user_pas,
                 new_user_date_reg):
        self.new_user_fn = new_user_fn
        self.new_user_ln = new_user_ln
        self.new_user_em = new_user_em
        self.new_user_phone = new_user_phone
        self.new_user_date_reg = new_user_date_reg
        self._new_user_pas = _new_user_pas


def user_registration():
    now = datetime.now()
    dt = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f" Enter your First name: ")
    new_user_fn = str(input()).upper()
    print(f" Enter your Last name: ")
    new_user_ln = str(input()).upper()
    print(f" Enter your email: ")
    new_user_em = input().upper()
    print(f" Enter your phone number: ")
    new_user_phone = str(input())
    new_user_date_reg = dt
    print(f" Enter your password: ")
    new_user_pas = str(input())
    new_user.append(new_user_pas)
    new_user.append(new_user_fn)
    new_user.append(new_user_ln)
    new_user.append(new_user_em)
    new_user.append(new_user_phone)
    new_user.append(new_user_date_reg)

    with open("users.csv", 'a+', newline="") as e:
        writer1 = csv.writer(e)
        writer1.writerow(new_user)
    e.close()


def user_login():
    print(f" Welcome to your profile! Please enter your Email: ")
    new_user_em = str(input()).upper()
    print(f" Enter your Password: ")
    new_user_pas = str(input())
    with open("users.csv", 'r') as user_file:
        data_reader = csv.reader(user_file, delimiter=',')
        details = [row for row in user_file if new_user_pas in row and new_user_em in row]
        if not details:
            print("Wrong credentials. Please try again")
            user_login()
        else:
            print(f"Welcome {new_user_em}")
            new_user_em = user_email
    user_window()


