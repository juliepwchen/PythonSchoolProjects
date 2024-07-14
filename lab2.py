#############################################################################
#   Name:       Julie Chen
#   Course:     CIS 41A
#   Project:    Lab 2
#   OS:         MacOS Sonoma 14.4.1
#   IDE:        Visual Studio Code 1.82.2
#   Compiler:   Python 3.12.1 [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
#   Shell:      zsh 5.9 (x86_64-apple-darwin23.0)
#############################################################################

#############################################################################
#   Task:       Plays a guess the number game with the user.
#   Description: 
#   1) The program asks the user for a range of numbers,
#   2) it randomly chooses a target number within the range. 
#   3) the program keeps asking the user to guess the target number 
#      until the user gets the correct number. 
#   4) For each guess, the program prints "guess higher" 
#      if the guess is below target number, 
#      or "guess lower" if the guess is above the target number. 
#   5) When the user guesses the correct number, 
#      the program prints the number of tries.
##############################################################################
import random

# function: main
# - prompts user to play guess game by 'y' or 'n'
# - play game until user ends the game
def main() :
    moreGame = input("Step 1: Want to play a guess a number game (y/n)? ")
    while (moreGame == 'y') :
        lower, upper = getRange()
        playOneGame(lower, upper)
        moreGame = input("Step 1: Want to play a guess a number game (y/n)? ")
        
# function: getRange
# - user sets the lower and upper ends of the range
#
# @return lower and upper ends of range
def getRange() :
    while True:
        lower = int(input("\tEnter lower end of range (>= 1): "))
        if lower < 1: 
            print(f"\tError! Invalid lower bound [{lower}]. Must be > or = 1.\n")
            continue
        upper = int(input("\tEnter upper end of range (<= 500): "))
        if upper > 500: 
            print(f"\tError! Invalid upper bound [{upper}]. Must be < or = 500. Start Over!\n")
            continue
        if (upper <= lower): 
            print(f"\tError! Upper [{upper}] must be > lower bound [{lower}]. Start Over!\n")
            continue
        return (lower, upper)
    
# function: getGuess
# - prompt user for a guess within a range
#
# @param lower: lower end of range
# @param upper: upper end of range
# @return a guess number with the range
def getGuess(lower, upper) :
    guess = int(input(f"Step 2: Guess a number between {lower} and {upper}, inclusive: "))
    while (guess < lower or guess > upper) :
        print(f"\tError! Invalid guess [{guess}]. Must be within {lower} and {upper} inclusive. Start Over!\n")
        guess = int(input(f"Step 2: Guess a number between {lower} and {upper}, inclusive: "))

    return guess

# function: playOneGame
# - user input a guess
#
# @param lower: lower end of range
# @param upper: upper end of range
# @return print the number of guesses 
def playOneGame(lower, upper) :
    target = random.randint(lower, upper)
    num_attempts = 0
    while True :
        guess = getGuess(lower, upper) 
        num_attempts += 1
        if num_attempts == 1 and guess != target: print(f"\tIncorrect Guess: {guess}")
        elif guess > target: print("\tGuess lower!")
        elif guess < target: print("\tGuess higher!")
        else: 
            print(f"\tCorrect guess [{guess}]! Your have attempted {num_attempts} guesses in this game!\n")
            break

main()