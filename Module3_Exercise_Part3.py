#############################################################################
#   Name:       Julie Chen
#   Course:     CIS 41A
#   Project:    Module 3 Exercise Part 3
#   OS:         MacOS Sonoma 14.4.1
#   IDE:        Visual Studio Code 1.82.2
#   Compiler:   Python 3.12.1 [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
#   Shell:      zsh 5.9 (x86_64-apple-darwin23.0)
#############################################################################

#############################################################################
#   Task:       Read file and process data.
#   Description: 
#   1) Read in the data from that file.
#   2) Store it as a dictionary of student name to an inner dictionary of 
#      class name to score.
#   3) Based on the data structure you created, allow user to prompt to 
#      ask for a student name. Print out the class name and score with the 
#      highest score for that student. If the user does not enter a valid 
#      student name, keep prompting until the student name is valid.
##############################################################################
def main():
    scores_filename = 'scores.txt'
    student_scores = read_scores(scores_filename)
    while True:
        student_name = input("Enter a student name: ")
        result = highest_scores(student_name, student_scores)
        if result:
            class_name, max_score = result
            print(f"Highest score for {student_name} is in {class_name} with a score of {max_score}")
            break
        else:
            print("Invalid student name. Please try again!")

# function: read_scores
# - map student name to a dictionary of class name to score.
# 
# @param filename - input date file
# @return student_scores - mapping table
def read_scores(filename):
    student_scores = {}
    with open (filename, 'r') as infile:
        for line in infile:
            data = line.strip().split(',')
            student_name = data[0]
            scores = {data[i]: int(data[i+1]) for i in range(1, len(data), 2)}
            student_scores[student_name] = scores
    return student_scores

# function: highest_scores
# - retrive the highest scores among the classes a student took
# 
# @param student_name - user input student name
# @ param student_scores - table of students and their scores
# @return classname - class name that has the higest score
#         max_score - maximum score among the classes
def highest_scores(student_name, student_scores):
    if student_name in student_scores:
        scores = student_scores[student_name]
        max_score = max(scores.values())
        class_name = [key for key, value in scores.items() if value == max_score][0]
        return class_name, max_score
    else:
        return None
    
main()


