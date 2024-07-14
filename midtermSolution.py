# Question 21
import csv

file_path = "records.csv"
student_records = []

try:
    with open(file_path, "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            student_records.append(row)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except IOError:
    print(f"Error reading file '{file_path}'.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Printing the student records
for record in student_records:
    print(record)

# Question 22
import statistics

def get_last_names_starting_with(letter, student_records):
    last_names = [record['name'].split()[-1] for record in student_records if record['name'].startswith(letter)]
    return last_names

def count_students_with_grade(course_name, grade, student_records):
    count = sum(1 for record in student_records if record['course'] == course_name and record['grade'] == grade)
    return count

def calculate_scores(course_name, student_records):
    scores = [float(record['score']) for record in student_records if record['course'] == course_name]
    average_score = round(sum(scores) / len(scores), 2) if scores else None
    median_score = round(statistics.median(scores), 2) if scores else None
    return {"average": average_score, "median": median_score}

# Question 23
class Movie:
    def __init__(self, line):
        parts = line.split(',')
        if len(parts) != 2:
            raise ValueError("Invalid movie format")

        self.title = parts[0].strip()
        try:
            self.rating = float(parts[1])
        except ValueError as e:
            raise ValueError("Invalid rating format") from e

    def __lt__(self, other):
        return self.rating < other.rating
    
# Question 24
class Hotel:
    def __init__(self, num_rooms, max_guests_per_room):
        self.num_rooms = num_rooms
        self.room_ids = [i for i in range(1, num_rooms + 1)]
        self.booked_rooms = {}
        self.max_guests_per_room = max_guests_per_room

    def book_room(self, num_guests):
        available_rooms = [room_id for room_id in self.room_ids if room_id not in self.booked_rooms]
        for room_id in available_rooms:
            if num_guests <= self.max_guests_per_room:
                self.booked_rooms[room_id] = num_guests
                return room_id
        return None

    def print_guests(self):
        print("Guests staying at the hotel:")
        for room_id, num_guests in self.booked_rooms.items():
            print(f"Room {room_id}: {num_guests} guests")

    def checkout(self, room_id):
        if room_id in self.booked_rooms:
            num_guests = self.booked_rooms.pop(room_id)
            rate = 80
            tax_rate = 0.09
            total_cost = rate * num_guests + rate * num_guests * tax_rate
            print(f"Room {room_id} checked out.")
            print(f"Total bill for Room {room_id}: ${total_cost:.2f}")
        else:
            print(f"Room {room_id} is not booked.")
    
# Question 25
class Restaurant(Hotel):
    def __init__(self, num_rooms, max_guests_per_room):
        super().__init__(num_rooms, max_guests_per_room)