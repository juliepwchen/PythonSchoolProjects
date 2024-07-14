##################################################################################
#   Name:       Julie Chen
#   Course:     CIS 41A
#   Project:    Exercise Module 2
#   OS:         MacOS Sonoma 14.4.1
#   IDE:        Visual Studio Code 1.82.2
#   Compiler:   Python 3.12.1 [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
#   Shell:      zsh 5.9 (x86_64-apple-darwin23.0)
###################################################################################

# Prompt the user for age. 
age = int(input("Enter your age: "))
# Based on the following conditions
# Below 7: G, 7 and up: PG, 13 and up: PG-13, 17 and up: R
# print out the highest level rated movie the person can watch:
if age >= 17:
    level = "R"
elif age >= 13:
    level = "PG-13"
elif age >= 7:
    level = "PG"
else: level = "G"

print(f"The highest level rated movie to watch is {level}.\n")

# Calculate the average of user-inputted positive numbers using a while loop. 
# Keep prompting the user to enter in more numbers until user enters -1.
count = 0
sum = 0.0
inputStr = input("Enter a positive number or -1 to finish: ")
while inputStr != "-1" :
    number = float(inputStr)
    count += 1
    sum += number
    inputStr = input("Enter a positive number or -1 to finish: ")

if (count > 0): average = sum / count
else : average = 0.0
print(f"The average is {(average):0.2f}\n")

# Ask the user for a phone number. 
# Loop through the string and make sure the number is in the format nnn-nnn-nnnn.
phone_number = input("Enter a phone number: ")
valid = len(phone_number) == 12
i = 0
while (valid and i < len(phone_number)):
    valid = phone_number[3] == "-" and phone_number[7] == "-" 
    if (i !=3 and i != 7): valid = phone_number[i].isdigit()
    i += 1

print(f"The phobe number is in valid format? {valid}\n")

# function: areaOfTriangle
# - calculate the area of a triangle
#
# @param base:  the base of a triangle
# @param height: the height of a triangle
# @return        the area of a triangle
def areaOfTriangle(base, height) :
    return (base * height) / 2

b = int(input("Enter the base of a triange: "))
h = int(input("Enter the height of a triange: "))
print(f"The Area of a Triangle with Base={b}, Height={h} is {areaOfTriangle(b, h):0.2f}\n")

# function: printFoodAndPrice
#
# @param food1:  first food name
# @param food2:  second food name
# @param price1: first price
# @param price2: second price
def printFoodAndPrice(food1, food2, price1, price2) :
    print(f"First Food: {food1}, price: {price1} \nSecond Food: {food2}, price: {price2}\n")

printFoodAndPrice("Peach", "Orange", 3.20, 1.20)

# function: sumOfOneToN
#
# @param food1:  first food name
# @param food2:  second food name
# @param price1: first price
# @param price2: second price
def sumOfOneToN(n) :
    if (n < 1): print("N must be >=1")
    elif (n == 1) : return 1
    else: return n + sumOfOneToN(n - 1)

print(f"The sume of N=5 is: {sumOfOneToN(5)}\n")