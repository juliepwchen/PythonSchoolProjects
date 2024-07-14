#############################################################################
#   Name:       Julie Chen
#   Course:     CIS 41A
#   Project:    Lab 5
#   OS:         MacOS Sonoma 14.4.1
#   IDE:        Visual Studio Code 1.82.2
#   Compiler:   Python 3.12.1 [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
#   Shell:      zsh 5.9 (x86_64-apple-darwin23.0)
#############################################################################

#############################################################################
#   Task:       Inheritance, Regular Expressions
#   Description: allow customers at a cafeteria to purchase food and drink
#   1) Customers are presented with a menu of several items of
#      a) hot food b) packaged food c) drinks, along with their prices.
#   2) Cusotmers choose the food/drink 
#   3) A receipt of all items, prices, and total amount is printed.
##############################################################################
from cafeteria import UI

def main():
    ui = UI("items.csv")

main()

