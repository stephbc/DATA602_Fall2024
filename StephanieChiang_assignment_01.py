#Q1 Fix all the syntax and logical errors in the given source code
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the
# average is a high score. The high score variable holds the value that is considered a high score.

high_score = 95

# Get the test scores.
test1 = input('Enter the score for test 1: ')
test2 = input('Enter the score for test 2: ')

#Missing the 3rd score input
test3 = input('Enter the score for test 3: ')

# Calculate the average test score.

#Fixed the order of operations
average = (test1 + test2 + test3) / 3

# Print the average.
print('The average score is', average)

# If the average is a high score,
# congratulate the user.

if average >= high_score:
    #Re-assign the high score to the user's average
    high_score = average
    #Clearer user messaging
    print('Congratulations! You have the best score!')
#Missing the else statement here will include both print statements (not necessarily undesirable though?)
else:
    print('That is a great average!')

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles.

rectangle_a_length = float(input('Enter the length of the first rectangle'))
rectangle_a_width = float(input('Enter the width of the first rectangle'))
rectangle_b_length = float(input('Enter the length of the second rectangle'))
rectangle_b_width = float(input('Enter the width of the second rectangle'))

nth = 'first'

def calc_area(length, width):
    area = length * width
    print('The area of the {nth} rectangle is', area)
    if nth == 'first':
        nth = 'second'

calc_area(rectangle_a_length, rectangle_a_width)
calc_area(rectangle_b_length, rectangle_b_width)

#Q3
#Ask a user to enter their first name and their age and assign it to the variables name and age.
#The variable name should be a string and the variable age should be an int.

name = input('Enter your first name')
age = int(input('Enter your age'))

#Using the variables name and age, print a message to the user stating something along the lines of:
# 'Happy birthday, name!  You are age years old today!'

print('Happy birthday, {name}! You are {age} years old today')
