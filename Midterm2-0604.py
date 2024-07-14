# Question 21: Read in all of this data into a data structure of your choice. Make sure that you do exception handling for files that don't open properly, can't read from, etc. I will give full credit for correct file reading and exception handling, but your data structure should be an appropriate choice to be able to complete the next problem.
def read_records(filename):

student_records = []

try:

with open(filename, 'r') as infile:

infile.readline() # skip first line: headers
lines = infile.readlines()
for line in lines:

fields = line.strip().split(',')

record = { 'ID': fields[0], 'name': fields[1],'year': int(fields[2]), 'course': fields[3], 'score': int(fields[4]), 'grade': fields[5] } student_records.append(record)

exceptFileNotFoundError:

print("Error: File not found.")

except Exception as e:

print(f"Error: {e}") return student_records

file_path = 'records.csv'

student_records = read_records(file_path)

print(student_records)

# Question 22: Write functions that can do the following on your previous data structure(s) from problem #21:

# A function that can grab all student last names that start with a particular letter given by the user and print those names out
# A function that takes in a course name and grade value (i.e. A+, C, B-, etc.) and print out how many students in that class earned that grade
# A function that takes in a course name and calculates the average score and median scores as doubles for that class and returns the values as a dictionary mapping "average" to the average score and "median" to the median score
ddef findStudentsLastnameStartWith(records, letter):

matches = [record['name'].split()[-1] for record in records if record['name'].split()[-1].startswith(letter)]

return matches 

def countStudentsByGrade(records, course, grade):

count = sum(1 for record in records if record['course'] == course and record['grade'] == grade)

return count

def calculateCourseStats(records, course):

scores = [record['score'] for record in records if record['course'] == course]

if not scores:

return None 

average = sum(scores) / len(scores)

sortedScores = sorted(scores)

n = len(sortedScores)

if n % 2 == 0:

median = (sortedScores[n // 2 - 1] + sortedScores[n // 2]) / 2

else:

median = sortedScores[n // 2]

return {'average': average, 'median': median}

# Question 23: Write a Movie class that will support the following code in main. You may use your discretion to create the class as you wish, but all of the following code must be supported:

# line = "Star Wars,2.23"

# movie1 = Movie(line)

# line = "The Lego Movie 2,9.16"

# movie2 = Movie(line)

# if movie1 < movie2:

#     print("first movie came out earlier")

# line = "Top Gun: Maverick,eleven"

# movie3 = Movie(line) # this line should cause an exception with the output: builtins.ValueError: could not convert string to float: 'eleven'
class Movie:

def __init__(self, line):

parts = line.split(',')

if len(parts) != 2:

raise ValueError("Invalid input format. Expected 'title,rating'.")

self.title = parts[0].strip()

try:

self.rating = float(parts[1].strip())

except ValueError:

raiseValueError("Invalid rating. Rating must be a number.")

def __lessThan__(self, other):

return self.rating < other.rating



# Question 24: Create a Hotel class that supports the following functionalities:

# The constructor should set up member variables that keep track of: number of rooms, room ids, which rooms are booked, how many guests can stay in each room
# A function to book a room. Should receive number of guests and look through available rooms, making sure that the room has enough space for that number of guests
# A function to print out list of all guests that are staying and the party size per guest
# A function that checks the guest out. The function should free up the hotel room. It should also print out a bill for the guest. The rate should be set to $80 per person, with a 9% tax rate.

class Hotel:

def __init__(self, num_rooms, max_guests):

self.num_rooms = num_rooms

self.roomIDs = [i for i in range(1, num_rooms + 1)]

self.bookedRooms = {}

self.maxGuests = max_guests

def bookRoom(self, num_guests):

for roomID in self.roomIDs:

if roomID not in self.bookedRooms or self.bookedRooms[roomID] + num_guests <= self.maxGuests:

self.bookedRooms[roomID] = self.bookedRooms.get(roomID, 0) + num_guests

return roomID

print("Sorry, no available room for {} guests.".format(num_guests))

return None

def printGuests(self):

print("Guests currently staying:")

for roomID, guests in self.bookedRooms.items():

print("Room {}: {} guests".format(roomID, guests))

def check_out(self, roomID):

if roomID in self.bookedRooms:

num_guests = self.bookedRooms[roomID]

total_bill = (num_guests * 80) * 1.09 

del self.bookedRooms[roomID]

print("Checked out from room {}.\nTotal bill: ${:.2f}".format(roomID, total_bill))

else:

print("Room {} is not booked.".format(roomID))