#############################################################################
#   Name:       Julie Chen
#   Course:     CIS 41A
#   Project:    Lab 4 - Restaurant Class
#   OS:         MacOS Sonoma 14.4.1
#   IDE:        Visual Studio Code 1.82.2
#   Compiler:   Python 3.12.1 [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
#   Shell:      zsh 5.9 (x86_64-apple-darwin23.0)
#############################################################################
#############################################################################
#   Description: 
#   Create a restaurant class with these operations as member functions:
#      - Add items to a menu.
#      - Make table reservations.
#      - Take customer orders.
#      - Print the menu.
#      - Print table reservations.
#      - Print customer orders.
##############################################################################
class Restaurant:

    def __init__(self, tables):
        self.__tables = {1: 3, 2: 5, 3: 10} if tables is None else tables
        self.__menu = {}
        self.__order = []
        self.__reservations = [False, False, False]

    def addToMenu(self, item, price):
        self.__menu[item] = price

    def printMenu(self):
        print(f"Restaurant Menu:")
        for item, price in self.__menu.items():
            print(f"Item: {item.title()}     ${price:0.2f}")
        print()

    # method: makeReservation
    # - determine if table is avilable for reservation
    # 
    # @param num_people - number of people dining
    # @return tableNumber if available, None if no table available
    def makeReservation(self, num_people):
        for tableNumber in range(len(self.__reservations)): 
            if self.__reservations[tableNumber] == False:
                if self.__tables[tableNumber+1] >= num_people:
                    self.__reservations[tableNumber] = True
                    return tableNumber+1
        return None
    
    # method: printAvailableReservations
    # - print out currenty available tabless
    # 
    def printAvailableReservations(self):
        count = 0
        for tableNum in range(len(self.__reservations)):
            if self.__reservations[tableNum] == False: 
                count += 1
                print(f"Table # {tableNum+1} is available with {self.__tables[tableNum+1]} seats.")
        print(f"There are {count} tables out of {len(self.__tables)} available!")
    
    # method: takeOrder
    # - take 1 item as part of the order 
    # 
    # @param item- an item ordered
    # @return - one order of items 
    def takeOrder(self, item):
        self.__order.append(item)

    # method: totalPrice
    # - calculate total price for all items ordered
    # 
    # @param order- items ordered
    def totalPrice(self):
        sum = 0
        for item in self.__order:
            if item in self.__menu:
                sum += self.__menu[item]
        return sum

    # getters and setters
    def getMenu(self):
        return self.__menu
    
    def getOrder(self):
        return self.__order