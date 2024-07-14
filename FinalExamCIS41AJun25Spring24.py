# Q24: Create a ChainRestaurant class that:

# Has a menu with at least 4 items on it with associated prices. You can designate these yourself.
# Has a list of cities of at least 5 locations that you can designate.
# Has a function to add new cities.
 

# Then, create a Franchise subclass that:

# Is a subclass of ChainRestaurant
# Has number of tables with number of seats per table, franchise price, location (city) attributes.
# Can add to the menu of the ChainRestaurant.
# Can take customer orders.
# class ChainRestaurant:

#     def __init__(self):

#         self.menu = { 'Energy Bar': 5.99, 'Coffee': 2.99, 'Kale': 1.99, 'Water': 0.99 }

#         self.cities = ['Silicon Valley', 'Austin', 'Chicago', 'Houston', 'Atlanta']

#     def addNewCity(self, city):

#         self.cities.append(city)




# class Franchise(ChainRestaurant):

#     def __init__(self, tables=None, franchise_price=None, location=None):

#         super().__init__()

#         self.tables = tables if tables else 20

#         self.seats_per_table = seats_per_table if seats_per_table else 2

#         self.franchise_price = franchise_price if franchise_price else 1000000

#         self.location = location

#     def add_to_menu(self, item, price):

#         super().add_to_menu(item, price)

#     def take_order(self, item):

#         if item in self.menu:

#             print(f"Order received for {item}.")

#         else:

#             print(f"Invalid order, {item} is not available on our menu.")

# Q23: This question is a continuation of the CIS class start times of the previous question.
# Suppose you have a pm list that has multiple start times, and each start time appears multiple
# times in the list.
# Example:  [ 3:30, 3:30, 6:00, 1:30, 3:30, 1:30, 1:30, ... ]


# Write a code segment to print each start time and the count of that start time in the list, sorted by start time.
# Ideally your code should not have to use an if statement, take advantage of Python features instead.
# But if the only way you can answer this question is with an if statement, go ahead and use the if statement.


# Example print out from the example list above:
# 1:30  3
# 3:30  3
# 6:00  1
# from collections import Counter

# amList, pmList = readAMPM(filehandler)

# count_dict = Counter(pmList)

# sortedTimes = sorted(count_dict.keys())

# for time in sortedTimes:

#     print(f"{time} {count_dict[time]}")

# Q22: Given that a text file has multiple lines of text.
# Each line contains the class name, section, days, and starting time of a CIS class. All lines are in
# the same format.
# One example lines is: 

# Python Programming: CIS 41A: TTh 6:00pm

# The file has been opened successfully with the statement:   
#        with open(filename) as f:


# Write a code segment that:
# -- uses the file handle f to read in data from the file
# -- stores all the starting times in 2 lists: an am list and a pm list


# With the example lines above, the am list will have:  11:30, 11:30
# and the pm list will have: 3:30, 6:00
# import re

# def readAMPM(filehandler):

#     amList = []

#     pmList = []

#     lines = filehandler.readlines()

#     pattern = r'(\d{1,2}:\d{2})(am|pm)'

#     for line in lines:

#         match = re.search(pattern, line, re.IGNORECASE)

#         if match: 

#             if match.group(2).lower() == 'am':

#                 amList.append(match.group(1))

#             elif match.group(2).lower() == 'pm':

#                 pmList.append(match.group(1))

#     return (amList, pmList)

# Q21: Given the following function header:
#      def count(*args, **kwargs) :
# Write code for the function count so that it prints the total number of arguments that are passed
# in.
# def count(*args, **kwargs):

#     print(f"Total number of arguments = { len(args) + len(kwargs) }")






