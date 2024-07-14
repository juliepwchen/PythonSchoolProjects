#############################################################################
#   Name:       Julie Chen
#   Course:     CIS 41A
#   Project:    Midterm #1 Review
#   OS:         MacOS Sonoma 14.4.1
#   IDE:        Visual Studio Code 1.82.2
#   Compiler:   Python 3.12.1 [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
#   Shell:      zsh 5.9 (x86_64-apple-darwin23.0)
#############################################################################
import random
import math
# Write a game that asks the user to guess a number between 1 and 10.
# The user should keep guessing until the right number is chosen. 
# Once the user wins, print out how many times it took for the user to win.
def game() :
    target = random.randint(1, 10)
    num_attempts = 0
    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        num_attempts += 1
        if (guess != target): continue
        else: break
    print(f"Correct, the right number is {target} and it took {num_attempts} tries")

#game()

# Write a function that calculates the hypotenuse of a right triangle 
# given the other two sides. The formula is a^2 + b^2 = c^2
def findHypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

print(f"The hypoteunes of a right triangle is {findHypotenuse(5, 6):0.2f}")

# Prompt the user to keep entering positive numbers until user enters -1. 
# After the user is finished, print out the smallest and largest numbers that 
# the user entered.
def findMinAndMax():
    num = int(input("Enter a positive number or -1 to terminate: "))
    min = num
    max = num
    while num != -1: 
        num = int(input("Enter a positive number or -1 to terminate: "))
        if num < min and num != -1: min = num
        elif num > max: max = num
    print (f"The Largest number is {max}, smallest number is {min}")

findMinAndMax()

# Ask the user for user's age and whether the user has had an accident in the past. 
# Depending on the user's responses, print out the insurance amount 
# subject to the following conditions:
#   16-35: $5000
#   36-49: $3000
#   50+: $2000
#   Accidents add $300 to the insurance.
def calculateInsurance():
    age = int(input("What is your age? "))
    hasAccidents = input("Has prior accidents (yes/no)? ")
    amount = 0
    if age >= 50: amount = 2000
    elif age >= 36: amount = 3000
    elif age >= 16: amount = 5000

    if (amount == 0): print("You are too young to drive!")
    elif (hasAccidents=="yes"): amount += 300
    return amount

print(f"The insurance amount: {calculateInsurance()}")

# Ask the user to provide a telephone number as a integer in the format nnnnnnnnnn (10 digits, no dashes).
# Use modulo and/or division as needed to break the 3 sections of the number into the format (nnn) nnn-nnnn 
# and print the result out as a string in that format.
def formatPhoneDigits():
    num = int(input("Enter a 10 digit number: "))
    lastFour = num % 10000
    middleThree = (num % 10000000 - lastFour) // 10000
    areaCode = (num % 10000000000 - middleThree - lastFour) // 10000000
    print(f"The new format is ({areaCode}) {middleThree}-{lastFour}")

formatPhoneDigits()

# area_code = phone_num // 10000000
# first_three = phone_num // 10000 % 1000
# last_four = phone_num % 10000