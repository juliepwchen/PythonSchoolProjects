from midterm2 import Fraction
import re

# Coding Question #1 
# Given a list called rainfall, which contains the yearly rainfall amount for different cities in California.
# Write code to print the average rainfall amount, with 1 digit after the decimal point.
rainfall = [0.12, 1.23, 3.45]
print(f"{sum(rainfall) / len(rainfall):.1f}")

# Coding Question #2
f = Fraction(4, 5)          # create a fraction with the value:  4/5
print(f)                    # prints:    4/5
num = float(f)           
print(num)                  # prints: 0.8
f = Fraction(3, 0)          # exception with output:    ZeroDivisionError: denominator can't be 0

# Coding Question #3
# Write code to create a list of fractions with the values: 1/2, 4/5, 2/3...
# where the numerator and denominators are from a set S, which is in the format:  {(1,2), (4,5), (2,3), ...}
S =  {(1,2), (4,5), (2,3), (5, 6) }
fractionList = []
for n,d in S :
    fractionList.append(Fraction(n,d))

# Read Code Question #1: Show the value of the variable output
a = ["orange", "apple", "kiwi", "banana"]
b = ["cake", "orange", "cookie", "banana", "candy"]
output = list(set(a) & set(b))
# Answer:   ['orange', 'banana']

# Read Code Question #2: what is the print out?
arr1 = [ [1, 2, 3], [4, 5, 6] ]       # A 2 row x 3 col table:   arr1[0] -> [ 1 , 2,  3] arr1[1] ->  [4 , 5,  6]
arr2 = arr1.copy()      # arr2 is a shallow copy of arr1: arr2[0] arr2[1]                 
# the outer list is different, but the inner lists are the same
arr3 = copy.deepcopy(arr1)            # arr3 is a separate, duplicate of arr1
(arr1[0][1], arr1[1][1]) = (10, 12)    # arr1 changes to:    [1,  10,  3] [4,  12,  6]
print(arr1)         
print(arr2)
print(arr3)
# Answer:     [ [1,10,3], [4,12,6] ] [ [1,10,3], [4,12,6] ] [ [1,2,3], [4,5,6] ]

# Read Code Question #3: the purpose of this block of code: except ValueError as eObject :
print(str(eObject))
# Answer: exception handling code, catch any ValueError exception and print the error message associated with the exception

# Read Code Question #3: what is the print out?
[x**2 for x in range(2,5)]
# will produce what data type and what are the value(s)?
# Answer: a list of integers:  [4, 9, 16]

{x**2 for x in range(2,5)}
# Answer: a set of integers: {4, 9, 16}, not necessarily in that order

# Read Code Question #4: what is the print out?
str1 = 'date: 02/10/2018'
print(re.findall('\d+',str1))
# Answer: ['02', '10', '2018']


