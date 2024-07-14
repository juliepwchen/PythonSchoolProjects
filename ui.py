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
#   Description: UI class
#   - user interface 
##############################################################################
import sys
from ranking import Ranking

class UI:
    def __init__(self):
        self.ranking = None

    # internal method: create_ranking_object
    # - create the Ranking object
    #
    def create_ranking_object(self):
        while self.ranking is None:
            try:
                filename = input("Enter the filename: ")
                self.ranking = Ranking(filename)
                print(f"Ranking for {len(self.ranking.getRankingData())} languages from {filename}")
            except Exception as e:
                print(f"Error opening file: {e}. Please try again.")
                self.ranking = None

    # internal method: view_by_ranking
    # - allow users to view, by ranking order, one language at a time
    # 
    def view_by_ranking(self):
        print("Printing one language at a time")
        print("After each language, press Enter to continue, any other key to stop")
        generator = self.ranking.languages_sorted_by_ranking()
        while True:
            try:
                number, language, rank = next(generator)
                print(f"{number}. {language:<20} {rank}")
                user_input = input()
                if user_input:  break
            except StopIteration:
                print("No more languages to display.")
                break

    # internal method: view_by_change
    # - allow users to view languages with positive/negative change, sorted by change order
    # 
    def view_by_change(self):
        while True:
            user_input = input("p. Positive change\nn. Negative change\nEnter Choice: ").strip().lower()
            if user_input in ['p', 'n']:
                positive = user_input == 'p'
                break
            else:
                print("Invalid input. Please enter 'p' for positive or 'n' for negative.")

        for language, change in self.ranking.languages_sorted_by_change(positive):
            print(f"{language:<20} {change}")

    # internal method: view_language_info
    # - allow users to view all info of one or more languages
    # 
    def view_language_info(self):
        user_input = input("Enter language names separated by commas: ").strip()
        languages = [lang.strip() for lang in user_input.split(',')]
        
        results = self.ranking.search_languages(*languages)
        print(f"     Language\t     Rank\tChange")
        for result in results:
            print(result)
    
    # method: run
    # - coordinates all the interactions with the user
    # 
    def run(self):
        self.create_ranking_object()

        menu = {
            'r': self.view_by_ranking,
            'c': self.view_by_change,
            'l': self.view_language_info,
            'q': sys.exit
        }

        while True:
            print("\nr. Languages by ranking")
            print("c. Languages by change")
            print("l. Language info")
            print("q. Quit")
            
            choice = input("Enter choice: ").strip().lower()
            action = menu.get(choice, None)
            if action:
                action()
            else:
                print("'r', 'c', 'l', or 'q' Only.")
        
UI().run()