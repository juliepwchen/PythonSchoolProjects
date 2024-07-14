# Final Exam CIS41A

# T         F           Q1. This code is a tuple comprehension:   (elem for elem in myList)
#                        F, it's a generator expression

# T        F           Q2. A child class overrides a parent class method by rewriting the method (providing a new
#                         implementation for the method).
#                         T

# T         F          Q3. Given var = {1,2,3,4,5,6,7,8,9,10}
#                      The following code will remove the first half of the values in var:     var = var[6:]
#                      F, var is a set and can't be accessed with [ ]

# T        F           Q4. The code:     print( set1.difference(set2) )
#                      will print all data values that are in set1 but not in set2
#                       T
 

# Read code.

# Q5: What's the output of the following code?         str1 = 'date is 02/10/2020, time is 10:59 ‘
#                                                      print(re.findall('\d+',str1))
# The list of all numbers, which are strings:  ['02', '10', '2020', '10', '59']

# Q6: Given:   myList = [1, 2, 3, 4, 5, 6]          
# Write one line of code to copy the values 3 and 4 from myList into a tuple called T
# T = tuple(myList[2:4])

# Q7: Given that the following code runs successfully
#        with open(“myfile.txt”) as infile :
#             for var1 in infile :
#                 var2 = var1.split()
#                 var3[var2[0]] = var2[1]

# What is the data type of var2?    list
# What is the data type of var2[1]  str
# What is the data type of var3?    dict
# If the file has data, what type of exception could happen in the code?
# IOError, IndexError, KeyError

# Q8: What does the following code print?
# def f1(text):
#      print(*text)         # unpacking

# def f2(*args):            # packing
#      print(len(args))
#      f1(args)

# f2("Python", "is", "awesome")
# f2("The end")

# 3
# Python is awesome
# 1
# The end

# Q0: Explain why you would want to use a generator instead of a comprehension with a very large sequence of data values.
# A comprehension will create a container of all the data values, which will take up a large amount of memory
# A generator will create one data value at a time so it takes up very little memory

# Write code

# Q10: Write a function that accepts a file handle named infile. 
# The file handle infile is successfully opened for reading from a file with multiple numbers, 
# one number per line. The function reads in numbers from the file and adds them to a Python container 
# if they aren't already in the container. The function stops reading the file when the container has 10 numbers, 
# then returns the numbers.
from typing import Any


def read10Nums(infile):
    S = set()                       # to keep numbers unique
    while len(S) < 10:
        line = infile.readline()
        S.add(float(line))           # float is more flexible than int
    return S      

# Q12: Write one line code to call the function above, and then write a second line of code to 
# print the 10 numbers on one line, sorted in reverse order, and with a comma separating the numbers.
S = read10Nums(filehandle) 
print(",".join(sorted(S, reverse=True)))

# Q13: Write a superclass Polygon that has 2 instance variables: n, the number of sides the polygon has                                                                                             
# lengths, a list of the length of each side

# poly = Polygon(3)                # line 1
# print(poly)                            # line 2
# print("Perimeter:", poly.perimeter())          #  line 3

# will run and produce the following output:
# Enter side 1: 1
# Enter side 2: 2
# Enter side 3: 3

# Polygon with 3 sides
# Perimeter: 6.0

class Polygon:
    def __init__(self, sides):
        self.__n = sides
        self.__lengths = []
        for side in range(self.__n):
            length = int(input(f"Enter side {side}: "))
            self.__lengths.append(length)

    def __repr__(self):
        print(f"Polygon with {self.__n} sides")

    def perimeter(self):
        return sum(self.__lengths)

# class Polygon:
#      def __init__(self, n) :       # line 1
#           self._n = n
#           self._lengths = []
#           for i in range(n) :
#                 size = float(input("Enter side: "))
#                 self._lengths.append(size)

#      def __repr__(self):                                                                                    # line 2
#           return “Polygon with “ + str(self._n) + “sides”

#      def perimeter(self):                                                                                  # line 3
#           return sum(self._lengths)

# Q14: Write a subclass Rectangle that is derived from Polygon, 
# such that the following code in main:

# rect = Rectangle()
# print(rect)
# print("Perimeter:", rect.perimeter())

# will run and produce the following output:
# Enter side 1: 3
# Enter side 2: 5
# Rectangle with 4 sides
# Perimeter: 16.0
    
class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)
        
    def __repr__(self):
        return f"Rectangle with 4 sides"
    
    def perimeter(self):
        return 2 * super().perimeter()

# class Rectangle(Polygon):
#       def __init__(self) :                                                                      
#           super().__init__(2)

#      def __repr__(self):                                                                      
#           return “Rectangle with “ + str(self._n * 2) + “sides”

#      def perimeter(self):                  # there are different ways to write this method                                                  
#           return 2 * super().perimeter()

 