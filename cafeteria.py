#############################################################################
#   Name:       Julie Chen
#   Course:     CIS 41A
#   Project:    Lab 5 -  Class
#   OS:         MacOS Sonoma 14.4.1
#   IDE:        Visual Studio Code 1.82.2
#   Compiler:   Python 3.12.1 [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
#   Shell:      zsh 5.9 (x86_64-apple-darwin23.0)
#############################################################################
import re

#############################################################################
#   Description: UI class
#   - user interface including functions:
#     a) print a menu, b) read in the user choices, c) prints the receipt.
##############################################################################
class UI:
    def __init__(self, filename):
        self.__uiMenu = {}      # an ordered refomatted menu
        self.__menuCount = 0
        try: 
            self._inventory = Inventory(filename)
            print(self._inventory.__repr__())

            self.uiMain()
        except IOError:
            print("Cannot open the file for read!")
        except Exception as e:
            print(f"Errors occur: {str(e)}")

    # method: menu
    # - print the menu
    def menu(self):
        self.__menuCount = 0
        print(f"Packaged food".center(22))
        for item in self._inventory.getPackagedFooeList():
            print(self._formatMenuItem_v2(item))
        print(f"Hot food".center(20))
        for item in self._inventory.getHotFoodList():
            print(self._formatMenuItem_v2(item))
        print(f"Drink".center(20))
        for item in self._inventory.getDrinksList(): 
            print(self._formatMenuItem_v2(item))

    # method: uiMain
    # - ask the user whether to continue to buy more food/drink
    def uiMain(self):
        option = ''
        while option != 'n':
            print()
            self.menu()
            self.takeOrders()
            option = input("\nBuy more? y/n: ").lower()

    # method: takeOrders
    # - allow user to order the food/drink
    # - use the input numbers to print each food/drink item
    # - its final price (including optional tax and CRV)
    # - print the total of all the items
    def takeOrders(self):
        userinput = input("\nEnter your choice numbers: ")
        sum = 0
        invalid = []
        orders = self._extraOrderNumbers(userinput)
        for order in orders:
            if 0 < int(order) <= self.__menuCount:
                print(f"{order}".ljust(2) + 
                        f"{self.__uiMenu[int(order)][0]}".ljust(12) + 
                        f"${self.__uiMenu[int(order)][2]:0.2f}".rjust(10))
                sum += self.__uiMenu[int(order)][2]
            else: 
                invalid.append(order)
        if sum > 0: print(f"Total: ${sum:0.2f}")
        if len(invalid) > 0: print("Invalid Choices: " + ', '.join(str(choice) for choice in invalid))

    # method: formatMenuItem_v2
    # - internal helper function to format a menu item for print 
    # - (Ex: 1 Granola Bar     $ 3.50)
    # - create a new menu list with order and total price
    #
    # @param count - menu number
    # @param item - a menu item
    # @return a formatted string
    def _formatMenuItem_v2(self, item):
        self.__menuCount += 1
        name, price = self._extractNameAndPrice(item.__repr__())
        self.__uiMenu[self.__menuCount] =  [ name, price, float(f"{item.getTotal():0.2f}")]  # create a new menu list
        return f"{self.__menuCount}".ljust(2) + f"{name}".ljust(12) + f"$ {price:0.2f}".rjust(10)
    
    # method: formatMenuItem_v1
    # - internal helper function to format a menu item for print
    # - (Ex: Granola Bar(10):3.5)
    #
    # @param count - menu number
    # @param item - a menu item
    # @return a formatted string
    def _formatMenuItem_v1(self, item):
        return item.__repr__()
        
    # method: extractNameAndPrice
    # - internal helper function to parse for Product Name and Price
    # 
    # @param str - original item.__repr__()
    # @return a tupple (Product Name, Price)
    def _extractNameAndPrice(self, str):
        pattern = r'(.+?)\(\d+\):(\d+(\.\d+)?)'
        match = re.match(pattern, str)
        if match:
            return (match.group(1).strip(), float(match.group(2)))
        else: return ( None, None )

    # method: extraOrderNumbers
    # - internal helper function to parse for order numbers
    # 
    # @param str - user input line
    # @return a list with order numbers
    def _extraOrderNumbers(self, str):
        pattern = r'-?\d+'
        order_numbers = re.findall(pattern, str)
        return order_numbers
    
    #getters and setters
    def getUIMenu(self): return self.__uiMenu

#############################################################################
#   Description: Inventory class
#   - reads in all foods and drinks from an input file 
#   - store all items in containers. 
##############################################################################
class Inventory:
    # method: totalPrice
    # - calculate total price for all items ordered
    # 
    # @param order- items ordered
    def __init__(self, filename):
        self.__packageList = []
        self.__hotfooList = []
        self.__drinksList = []

        try:
            with open(filename, 'r') as infile:
                lines = infile.readlines()
                for line in lines:
                    fields = line.strip().split(',')
                    try: 
                        code = int(fields[0])
                        price = float(fields[2])
                    except: raise ValueError("Invalid Food Code or Price within the input file.")

                    name = fields[1]
                    drinksize = fields[3] if fields[3] == 'S' or 'L' else None
                    if 10 <= code <=19: 
                        self.__packageList.append(PackagedFood(code, name, price))
                    elif 20 <= code <= 29: 
                        self.__hotfooList.append(HotFood(code, name, price))
                    elif 30 <= code <= 39: 
                        self.__drinksList.append(Drink(code, name, price, drinksize))
                    else:
                        raise ValueError(f"Invalid Food Code {code} in line: {line}")
        except IOError:
            print("Cannot open the file for read!")
        except ValueError as e:
            print(f"Value Errors: {str(e)}")
        except Exception as e:
            print(f"Errors occur when opening or reading the file: {str(e)}")

    # method: totalPrice
    # - calculate total price for all items ordered
    # 
    # @param order- items ordered
    def  __repr__(self):
        return (f"{len(self.__packageList)} packaged foods, {len(self.__hotfooList)} hot foods, {len(self.__drinksList)} drinks")
    
    # getters and setters
    def getPackagedFooeList(self): return self. __packageList
    def getHotFoodList(self): return self.__hotfooList
    def getDrinksList(self): return self.__drinksList

#############################################################################
#   Description: Salem class
#   - food that are prepackaged (such as a bag of chips or a boxed salad)
##############################################################################
class SaleItem:
    TAX_RATE = 0.0913
    def __init__(self, code, name, price):
        self.__code = code
        self.__productname = name
        self.__price = price

    def  __repr__(self):
        return f"{self.__productname} ({self.__code}): {self.__price:0.2f}"
    
    #getters and setters
    def getCode(self): return self.__code
    def getProductName(self): return self.__productname
    def getPrice(self): return self.__price
    def getTaxRate(self): return self.TAX_RATE

#############################################################################
#   Description: PackagedFood class
#   - food that are prepackaged (such as a bag of chips or a boxed salad)
##############################################################################
class PackagedFood(SaleItem):
    def __init__(self, code, name, price):
        super().__init__(code, name, price)
        self.__total = price
        
    def  __repr__(self):
        return f"{self.getProductName()} ({self.getCode()}):{self.getPrice():0.1f}"

    #getters and setters
    def getTotal(self): return self.__total
    
#############################################################################
#   Description: HotFood class
#   -  food that are prepared and heated (like pizza)
##############################################################################
class HotFood(SaleItem):
    def __init__(self, code, name, price):
        super().__init__(code, name, price)
        self.__total = (1 +  self.getTaxRate()) * price
        
    def  __repr__(self):
        return f"{self.getProductName()} ({self.getCode()}):{self.getPrice():0.1f} - heated\n{(self.__total):0.2f}"

    #getters and setters
    def getTotal(self): return self.__total

#############################################################################
#   Description: Drink class
#   -  bottled or canned drinks
##############################################################################
class Drink(SaleItem):
    CRV_SMALL = 0.05
    CRV_LARGE = 0.10

    def __init__(self, code, name, price, drinksize):
        super().__init__(code, name, price)
        self.__total = (1 +  self.getTaxRate()) * (price + (self.CRV_LARGE if drinksize == 'L' else self.CRV_SMALL))

    def  __repr__(self):
        return f"{self.getProductName()} ({self.getCode()}):{self.getPrice():0.1f}\n{self.__total:0.2f}"
    
    #getters and setters
    def getTotal(self): return self.__total