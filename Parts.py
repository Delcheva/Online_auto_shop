from orders import *

header = ['ID', 'Part Name', "Category", "Compatible Models", "Price", "Original_Price"]

PART_BASE = "parts.xls"
new_item = []


class CarParts:
    def __init__(self, id_parts, engine, transmission, break_system):
        self.id_parts = id_parts
        self._engine = engine
        self._transmission = transmission
        self.break_system = break_system


def main_selections_of_parts():
    print(f"Please choose from the section below:")
    print(f"1 - Engine")
    print(f"2 - Transmission")
    print(f"3 - BreakSystem")
    print(f"4 - Fill cart")
    print(f"5 - Exit")
    user_input = str(input())
    if user_input == "1":
        main_engine_choices()
    elif user_input == "2":
        main_transmission_choices()
    elif user_input == "3":
        main_break_system_parts()
    elif user_input == "4":
        fill_cart()
        display_order()
    elif user_input == "5":
        exit()
    else:
        print("Please make correct option!")
        main_break_system_parts()


class Engine(CarParts):
    def __init__(self, strap, gasket, suspension, oil_filter, water_pump, fuel_filter):
        self.strap = strap
        self.gasket = gasket
        self.suspension = suspension
        self.oil_filter = oil_filter
        self.water_pump = water_pump
        self.fuel_filter = fuel_filter


def main_engine_choices():
    print(f"You are at the Engine parts menu! The parts we have available for now are: ")
    print("1- Strap")
    print("2- Gasket")
    print("3- Suspension")
    print("4- Oil Filter")
    print("5- Water pump")
    print("6- Fuel filter")
    print("7- Return to menu")
    print("Please make a choice: ")
    user_input = str(input())
    if user_input == "1":
        strap_available()
    elif user_input == "2":
        gasket_available()
    elif user_input == "3":
        suspension_available()
    elif user_input == "4":
        oil_available()
    elif user_input == "5":
        water_available()
    elif user_input == "6":
        fuel_available()
    elif user_input == "7":
        main_selections_of_parts()
    else:
        print("Please enter a valid choice! ")
        main_engine_choices()


new_part_item = []
new_part_item2 = []


def strap_available():
    with open("parts.csv", 'r') as file_:
        data_reader = csv.reader(file_)
        count = 0
        for row in data_reader:
            if row[1] == "Strap":
                print(*row[0:-1])
                count += 1
            elif count > 2:
                break
    print(f"If you want to go back - please enter 0")
    user_input = str(input())
    if user_input == "0":
        main_engine_choices()
    else:
        print("Please make correct option.")
        strap_available()


def suspension_available():
    with open("parts.csv", 'r') as file0:
        data_reader = csv.reader(file0)
        count = 0
        for row in data_reader:
            if row[1] == "Suspension":
                print(*row[0:-1])
                count += 1
            elif count > 2:
                break
    print(f"If you want to go back - please enter 0")
    user_input = str(input())
    if user_input == "0":
        main_engine_choices()
    else:
        print("Please make correct option.")
        suspension_available()


def gasket_available():
    with open("parts.csv", 'r') as file1:
        data_reader = csv.reader(file1)
        count = 0
        for row in data_reader:
            if row[1] == "Gasket":
                print(*row[0:-1])
                count += 1
            elif count > 2:
                break
    print(f"If you want to go back - please enter 0")
    user_input = str(input())
    if user_input == "0":
        main_engine_choices()
    else:
        print("Please make correct option.")
        gasket_available()


def oil_available():
    with open("parts.csv", 'r') as file2:
        data_reader = csv.reader(file2)
        count = 0
        for row in data_reader:
            if row[1] == "Oil filter":
                print(*row[0:-1])
                count += 1
            elif count > 2:
                break
    print(f"If you want to go back - please enter 0")
    user_input = str(input())
    if user_input == "0":
        main_engine_choices()
    else:
        print("Please make correct option.")
        oil_available()


def water_available():
    with open("parts.csv", 'r') as file3:
        data_reader = csv.reader(file3)
        count = 0
        for row in data_reader:
            if row[1] == "Water pump":
                print(*row[0:-1])
                count += 1
            elif count > 2:
                break
    print(f"If you want to go back - please enter 0")
    user_input = str(input())
    if user_input == "0":
        main_engine_choices()
    else:
        print("Please make correct option.")
        water_available()


def fuel_available():
    with open("parts.csv", 'r') as file4:
        data_reader = csv.reader(file4)
        count = 0
        for row in data_reader:
            if row[1] == "Fuel filter":
                print(*row[0:-1])
                count += 1
            elif count > 2:
                break
    print(f"If you want to go back - please enter 0")
    user_input = str(input())
    if user_input == "0":
        main_engine_choices()
    else:
        print("Please make correct option.")
        fuel_available()


class Transmission(CarParts):
    def __init__(self, connector_wire, flywheel_disk, clutch_pedal):
        self.connector_wire = connector_wire
        self.flywheel_disk = flywheel_disk
        self.clutch_pedal = clutch_pedal


def main_transmission_choices():
    print(f"You are at the Transmission parts menu! The parts we have available for now are: ")
    print("1- Connector wire")
    print("2- Flywheel disk")
    print("3- Clutch pedal")
    print("4 - Return")
    print("Please make a choice: ")
    user_input = str(input())
    if user_input == "1":
        connector_available()
    elif user_input == "2":
        flywheel_available()
    elif user_input == "3":
        clutch_available()
    elif user_input == "4":
        main_selections_of_parts()
    else:
        print("Please enter valid choice! ")
        main_transmission_choices()


def connector_available():
    with open("parts.csv", 'r') as file5:
        data_reader = csv.reader(file5)
        count = 0
        for row in data_reader:
            if row[1] == "Connector wire":
                print(*row[0:-1])
                count += 1
            elif count > 2:
                break
    print(f"If you want to go back - please enter 0")
    user_input = str(input())
    if user_input == "0":
        main_transmission_choices()
    else:
        print("Please make correct option.")
        connector_available()


def flywheel_available():
    with open("parts.csv", 'r') as file6:
        data_reader = csv.reader(file6)
        count = 0
        for row in data_reader:
            if row[1] == "Flywheel disk":
                print(*row[0:-1])
                count += 1
            elif count > 2:
                break
    print(f"If you want to go back - please enter 0")
    user_input = str(input())
    if user_input == "0":
        main_transmission_choices()
    else:
        print("Please make correct option.")
        flywheel_available()


def clutch_available():
    with open("parts.csv", 'r') as file7:
        data_reader = csv.reader(file7)
        count = 0
        for row in data_reader:
            if row[1] == "Clutch pedal":
                print(*row[0:-1])
                count += 1
            elif count > 2:
                break
    print(f"If you want to go back - please enter 0")
    user_input = str(input())
    if user_input == "0":
        main_transmission_choices()
    else:
        print("Please make correct option.")
        clutch_available()


class BreakSystem(CarParts):
    def __init__(self, brake_disks, brake_hoses, brake_drum):
        self.brake_disks = brake_disks
        self.brake_hoses = brake_hoses
        self.brake_drum = brake_drum


def main_break_system_parts():
    print(f"You are at the BreakSystem parts menu! The parts we have available for now are: ")
    print("1- Brake disks")
    print("2- Brake hoses")
    print("3- Break drum")
    print("4- Return")
    print("Please make a choice: ")
    user_input = str(input())
    if user_input == "1":
        disks_available()
    elif user_input == "2":
        hoses_available()
    elif user_input == "3":
        drum_available()
    elif user_input == "4":
        main_selections_of_parts()
    else:
        print("Please enter valid choice! ")
        main_break_system_parts()


def disks_available():
    with open("parts.csv", 'r') as file8:
        data_reader = csv.reader(file8)
        count = 0
        for row in data_reader:
            if row[1] == "Brake disks":
                print(*row[0:-1])
                count += 1
            elif count > 2:
                break
    print(f"If you want to go back - please enter 0")
    user_input = str(input())
    if user_input == "0":
        main_break_system_parts()
    else:
        print("Please make correct option.")
        disks_available()


def hoses_available():
    with open("parts.csv", 'r') as file9:
        data_reader = csv.reader(file9)
        count = 0
        for row in data_reader:
            if row[1] == "Brake hoses":
                print(*row[0:-1])
                count += 1
            elif count > 2:
                break
    print(f"If you want to go back - please enter 0")
    user_input = str(input())
    if user_input == "0":
        main_break_system_parts()
    else:
        print("Please make correct option.")
        hoses_available()


def drum_available():
    with open("parts.csv", 'r') as file10:
        data_reader = csv.reader(file10)
        count = 0
        for row in data_reader:
            if row[1] == "Brake drum":
                print(*row[0:-1])
                count += 1
            elif count > 2:
                break

    print(f"If you want to go back - please enter 0")
    user_input = str(input())
    if user_input == "0":
        main_break_system_parts()
    else:
        print("Please make correct option.")
        drum_available()


