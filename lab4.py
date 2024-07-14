#############################################################################
#   Name:       Julie Chen
#   Course:     CIS 41A
#   Project:    Lab 4
#   OS:         MacOS Sonoma 14.4.1
#   IDE:        Visual Studio Code 1.82.2
#   Compiler:   Python 3.12.1 [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
#   Shell:      zsh 5.9 (x86_64-apple-darwin23.0)
#############################################################################
#############################################################################
#   Task:       Classes and Objects
#   Description: 
#   1) User prompt for inputting all of the items and adding to a menu.
#   2) Printing the menu
#   3) Print table reservations
#   4) To take customer orders, print out the menu and ask user for as many 
#      orders as user wants. Then the function should print out the total
#      price for the user of all items ordered.
##############################################################################
from restaurant import Restaurant

rest1 = Restaurant(None)
print("Step 1: We start by creating the menu for the restaurant.")
while True:
    item = input("\tEnter a menu item or 'Q' to quit: ").lower()
    if item == 'q': break
    price = float(input("\tEnter the price for the menu item: "))
    rest1.addToMenu(item, price)

rest1.printMenu()

print("Step 2: Make Reservations for the customers.")
numOfPeople = int(input("\tEnter number of people dining? "))
tableNum = rest1.makeReservation(numOfPeople)
format_msg = f"\tYour Table is #{tableNum}\n" if tableNum is not None else "\tWe do not have table to accomendate you!\n"
print(format_msg)

# show available tables
print("For the restaurant staff:")
rest1.printAvailableReservations()
print()

# take orders
print("Step 3: To order, here is the menu:")
rest1.printMenu()
while True:
    item = input("\tEnter item(s) you like to order or 'Q' to finish: ").lower()
    if item != 'q':
        rest1.takeOrder(item)
    else: break

order = rest1.getOrder() 
total = rest1.totalPrice()
print(f"The total price for your order is ${total:0.2f}")

