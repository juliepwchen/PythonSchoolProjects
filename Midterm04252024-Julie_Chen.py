#############################################################################
#   Name:       Julie Chen
#   Course:     CIS 41A
#   Project:    Midterm - April 25, 2024
#   OS:         MacOS Sonoma 14.4.1
#   IDE:        Visual Studio Code 1.82.2
#   Compiler:   Python 3.12.1 [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
#   Shell:      zsh 5.9 (x86_64-apple-darwin23.0)
#############################################################################

# Problem #1: Write 2 functions that calculate the surface area and volume of a cube. 
# The surface area of a cube is 6 times the area of one side (calculated by squaring 
# the length of the side). The volume of a cube is the length of one side cubed.
def cubeSurfaceArea(side):
    return (side**2) *6
def cubeVolume(side): 
    return side**3

# Problem #2 Prompt the user to keep entering in floating point numbers until the user enters 0. 
# After the user is done, calculate the difference between the greatest and least values
# that were entered and print them out.
def findMinAndMax():
    # when convert float to int, fraction part is lost
    EPSILON = 1E-14

    num = float(input("Enter a floating number or 0 to terminate: "))
    if abs(num - 0.0) < EPSILON:
        print("No numbers werer entered!")
        return
    min = num
    max = num
    while True:
        num = float(input("Enter a floating number or 0 to terminate: "))
        if abs(num - 0.0) < EPSILON:
            print("No numbers werer entered!")
            break
        if num < min - EPSILON: min = num
        elif num > max + EPSILON: max = num
        
    print (f"difference = {(max - min):0.2f}")

findMinAndMax()

# Problem #3: Prompt the user for the number of years (a positive whole number) 
# that a monarch of a country has reigned. If the monarch reigned for 25 years, print that 
# it's the silver jubilee. If the monarch reigned for 50 years, print that it's the golden jubilee. 
# If the monarch reigned for 60 years, print that it's the diamond jubilee. For any other number, 
# print the number of years until the next jubilee and what jubilee it is. You can assume that the 
# user will enter in a positive whole number; you don't need to do input validation.
def calculateJubilee(years):
    if years >= 60:
        print(f"The monarch has reigned for {years} years. It's the diamond jubilee!")
    elif years >= 50:
        print(f"The monarch has reigned for {years} years. It's the golden jubilee!")
    elif years >= 25:
        print(f"The monarch has reigned for {years} years. It's the silver jubilee!")
    else:
        next_jubilee = 25 if years < 25 else 50 if years < 50 else 60
        years_until_next_jubilee = next_jubilee - years
        print(f"The monarch has reigned for {years} years.")
        print(f"Next jubilee is in {years_until_next_jubilee} years. It will be the {'silver' if next_jubilee == 25 else 'golden' if next_jubilee == 50 else 'diamond'} jubilee!")

def main():
    years = int(input("Enter the number of years the monarch has reigned: "))
    calculateJubilee(years)

main()

def justinSolution3():
    num_years = int(input("How many years has the monarch reigned?"))
    if num_years == 25:
        print("silver jubilee")
    elif num_years == 50:
        print("golden jubilee")
    elif num_years == 60:
        print("diamond jubliee")
    elif 0 <= num_years < 25:
        print(25 - num_years, "until silver jubliee")
    elif 25 < num_years < 50:
        print(50 - num_years, "until golden jubliee")
    elif 50 < num_years < 60:
        print(60 - num_years, "until diamond jubliee")

# Problem #4: Ask the user for a 7 digit phone number as a string in the format nnn-nnnn. 
# Use type conversions and division and/or modulo to get the two parts of the number as nnn and nnnn. 
# Print out the difference between the two numbers and the quotient between the two numbers. 
# The quotient should be a floating point number.
def julieSolution4():
    phone_number = input("Enter a 7-digit phone number in the format nnn-nnnn: ")
    parts = phone_number.split('-')
    if len(parts) != 2 or len(parts[0]) != 3 or len(parts[1]) != 4:
        print("Invalid phone number format. Please enter a 7-digit number in the format nnn-nnnn.")
        return
    firstThree = int(parts[0]) 
    lastFour = int(parts[1]) 
    difference = lastFour - firstThree
    quotient = lastFour / firstThree
    print(f"Difference between the two parts ({lastFour} - {firstThree}): {difference}")
    print(f"Quotient of the two parts ({lastFour} / {firstThree}): {quotient:.2f}") 

def justinSolution4():
    phone_num = input("Enter a 7-digit phone number in the format nnn-nnnn: ")
    first_three= int(phone_num[0:3])
    last_four = int(phone_num[4:])
    print(f"Difference : {first_three - last_four}")
    print(f"Quotient : {(first_three / last_four):0.2f}") 

# Problem #5: Write a program that asks the user to guess a word. Ignore casing 
# (lowercase or uppercase doesn't matter). The program will keep prompting the user 
# to guess the word until the user gets it right. The program should tell the user 
# how many letters the word is, and on each guess tell the user how many letters were correct. 
# To be a correct letter, the letter must be the same letter as the mystery word and the 
# same position in the word. You can use any mystery word you want.
import random
def guessWordGame():
    words = ["orange", "seaweed", "julie", "deAnza", "iphone", "macbook", "samsung"]
    randomWord = random.choice(words).lower() 
    word_length = len(randomWord)
    print("You have entered the Guess the Word game!")
    print(f"The random word has {word_length} letters.")
    while True:
        guess = input("Enter your guess (a word): ").lower() 
        if guess == randomWord:
            print(f"Correct! The random word is '{randomWord}'!")
            break
        else:
            if len(guess) != word_length:
                print(f"The guess word should be {word_length} letters long. Try again.")
                continue
            for i in range(len(guess)):
                if guess[i] == randomWord[i]: num_correct += 1
                print(f"Incorrect Guess. Only {num_correct} letters are correct.")

guessWordGame()

def justinSolution5():
    mystery_word = "test"
    print(f"The mystery word has {len(mystery_word)} letters.")
    guess = input("Guess the mystery word?").lower()
    while (guess != mystery_word): 
        count = 0
        for i in range(len(mystery_word)):
            if guess[i] == mystery_word[i]:
                count += 1
        print(f"You guessed {count} letters correctly out of {len(mystery_word)}")

    print("You got the myster word correctly! The word is {guess}")
            

