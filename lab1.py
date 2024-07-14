##################################################################################
#   Name:       Julie Chen
#   Course:     CIS 41A
#   Project:    Lab 1 - Practice on numbers, strings, arithmetic operators, IO
#   OS:         MacOS Sonoma 14.4.1
#   IDE:        Visual Studio Code 1.82.2
#   Compiler:   Python 3.12.1 [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
#   Shell:      zsh 5.9 (x86_64-apple-darwin23.0)
###################################################################################

##################################################################################
#   Task:       Part I
#   Assumption: 
#   For this exercise, I assume that in the final output, there is exactly one space 
#   between the first and last name when displayed inside the box.
#     - When calculating left and right padding based on this assumption, 
#       the logic follows using the default split() method on the full name to 
#       remove all unnecessary spaces (e.g., whitespace, tabs, newlines). Then
#       format using f-string by leaving 1 space between first and last name.
###################################################################################
# Create a constant named MAX and set it to 40
MAX = 40
# Prompt and read in the user’s name.
full_name = input("Enter your name: ")
# Ask the user for the number of previous programming classes taken
num_courses = int(input("Enter the number of programming classes you've taken: "))
# Ask the user for their goal when taking the CIS 41A class
goal = input("Enter the goal you have for this class: ")
# Print a blank line
print()
# Print the user’s name in a box
# - print line of MAX number of asterisks (*)
print("*" * MAX)
# - print a line with * at both ends, and a number of spaces in between.
BORDER_WIDTH = 1
INNER_BOX_WIDTH = MAX - 2 * BORDER_WIDTH
formatted_string = f"*{' ' * INNER_BOX_WIDTH}*"
print(formatted_string)
# - print a line with * at both ends, and the user’s name centered
first_name, last_name = full_name.split()
left_padding = (INNER_BOX_WIDTH - len(first_name + ' ' + last_name)) // 2
right_padding = INNER_BOX_WIDTH - len(first_name + ' ' + last_name) - left_padding
formatted_string = f"*{' ' * left_padding}{first_name.capitalize()} {last_name.capitalize()}{' ' * right_padding}*"
print(formatted_string)
# - print A line with * at both ends, and a number of spaces in between.
formatted_string = f"*{' ' * INNER_BOX_WIDTH}*"
print(formatted_string)
# - print line of MAX number of asterisks (*)
print("*" * MAX)
# - print the number of programming classes taken, with explanation text. 
print("You've taken %d programming classes" %(num_courses))
# - print a header line of text, then print the user’s goal for taking CIS 41A on a second line.
print("Your goal for this class is: \n%s" %(goal.upper()))

##################################################################################
#   Task:    Part II
###################################################################################
# Enter your name: julie chen    
# Enter the number of programming classes you've taken: 3 
# Enter the goal you have for this class: Preparation for entering a data analytics specialization.

# ****************************************
# *                                      *
# *              Julie Chen              *
# *                                      *
# ****************************************
# You've taken 3 programming classes
# Your goal for this class is: 
# PREPARATION FOR ENTERING A DATA ANALYTICS SPECIALIZATION.

##################################################################################
#   Task:    Part III
###################################################################################
# Enter your name: julie     che
# Enter the number of programming classes you've taken: 3
# Enter the goal you have for this class: prePAre fOR eNTERinG A daTA anALyticS sPECiaLiZAtion!

# ****************************************
# *                                      *
# *              Julie Che               *
# *                                      *
# ****************************************
# You've taken 3 programming classes
# Your goal for this class is: 
# PREPARE FOR ENTERING A DATA ANALYTICS SPECIALIZATION!