# Stephanie Chiang, Week 2 Assignment

# Q1. What will the following code display?
numbers = [1, 2, 3, 4, 5]
print(numbers[1:-5])

# MY ANSWER: The above code prints an empty array.

# Can you debug and fix the output? The code should return the entire list

print(numbers)
# or
print(numbers[0:])
# or
print(numbers[:5])
# or
print(numbers[:])

# Q2. Design a program that asks the user to enter a store’s sales for each day of the
# week. The amounts should be stored in a list. Use a loop to calculate the total sales for
# the week and display the result.

sales = []
for i in range(7):
  day = input("Enter sales for day " + str(i+1) + ": ")
  sales.append(day)

total = 0
for num in sales:
  total += int(num)
print("Total sales for the week: " + str(total))

# Q3. Create a list with at least 5 places you’d like to travel to. Make sure the list isn’t in
# alphabetical order
# ● Print your list in its original order.
# ● Use the sort() function to arrange your list in order and reprint your list.
# ● Use the sort(reverse=True) and reprint your list.

travel_plans = ['Norway', 'China', 'Taiwan', 'Australia', 'New Zealand', 'Azores', 'Portugal', 'Spain']
print(travel_plans)
travel_plans.sort()
print(travel_plans)
travel_plans.sort(reverse=True)
print(travel_plans)

# Q4. Write a program that creates a dictionary containing course numbers and the room
# numbers of the rooms where the courses meet. The program should also create a
# dictionary containing course numbers and the names of the instructors that teach each
# course. After that, the program should let the user enter a course number, then it should
# display the course’s room number, instructor, and meeting time.

course_locations = {
  'DATA606': 'Room 1',
  'DATA607': 'Room 2',
  'DATA602': 'Room 3',
}

course_instructors = {
  'DATA606': 'Prof A',
  'DATA607': 'Prof B',
  'DATA602': 'Prof C',
}

# This question does not specify if the meeting time is another dictionary or part of an existing one?
meeting_time = 'asynchronous'

my_course = input('Enter the course number: ')
print(f"Course {my_course} meets at {course_locations[my_course]} with {course_instructors[my_course]}. The schedule is {meeting_time}.")

# Q5. Write a program that keeps names and email addresses in a dictionary as
# key-value pairs. The program should then demonstrate the four options:
# ● look up a person’s email address,
# ● add a new name and email address,
# ● change an existing email address, and
# ● delete an existing name and email address.

contacts = { 'Alex': 'alex@example.com', 'Billie': 'billie@example.com' }

def find_email(name):
  if name in contacts:
    print(contacts[name])
  else:
    print('Contact not found. Please try again.')

def add_contact(name, email):
  contacts[name] = email

def change_email(name, new_email):
  if name in contacts:
    contacts[name] = new_email
    print('Email address updated.')
  else:
    print('Contact not found. Please try again.')

def delete_contact(name):
  if name in contacts:
    del contacts[name]
    print('Contact deleted.')
  else:
    print('Contact not found. Please try again.')

# Testing
find_email('Alex')  # Output: alex@example.com
add_contact('Charlie', 'charlie@example.com')
find_email('Charlie')  # Output: charlie@example.com
change_email('Alex', 'new_alex@example.com')
find_email('Alex')  # Output: new_alex@example.com
delete_contact('Billie')
find_email('Billie')  # Output: Contact not found. Please try again.
print(contacts)
