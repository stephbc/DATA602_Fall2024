# Stephanie Chiang
# DATA 602 Fall 2024
# Assignment 3

# Q1: Write a program that prompts the user for a meal: breakfast, lunch, or dinner. Then using if statements and else statements print the user a message recommending a meal. For example, if the meal was breakfast, you could say something like, “How about some bacon and eggs?”
# The user may enter something else in, but you only have to respond to breakfast, lunch, or dinner.

def meal():
  meal_time = input("Breakfast, lunch, or dinner? ").lower()

  if meal_time == 'breakfast':
    print("How about coffee and a smoothie?")
  elif meal_time == 'lunch':
    print("How about instant ramen with egg and veggies?")
  elif meal_time == 'dinner':
    print("How about pork and cabbage stew with rice?")
  else:
    print("That's not a meal time!")

meal()


# Q2: The mailroom has asked you to design a simple payroll program that calculates a student employee’s gross pay, including any overtime wages. If any employee works over 20 hours in a week, the mailroom pays them 1.5 times their regular hourly pay rate for all hours over 20.
# You should take in the user’s input for the number of hours worked, and their rate of pay.

def payroll():
  hours = float(input("Enter the number of hours worked: "))
  rate = float(input("Enter the hourly rate: "))

  if hours > 20:
    gross_pay = (20 * rate) + ((hours - 20) * (rate * 1.5))
  else:
    gross_pay = hours * rate
  print(gross_pay)

payroll()


# Q3: Write a function named times_ten. The function should accept an argument and display the product of its argument multiplied times 10.

def times_ten(num):
  print(float(num) * 10)


# SQ4: Find the errors, debug the program, and then execute to show the output.

# def main()
#       Calories1 = input( "How many calories are in the first food?")
#       Calories2 = input( "How many calories are in the first food?")
#       showCalories(calories1, calories2)

# def showCalories()
#    print(“The total calories you ate today”, format(calories1 + calories2,.2f))

def main():
  calories1 = int(input("How many calories are in the first food? "))
  calories2 = int(input("How many calories are in the second food? "))
  showCalories(calories1, calories2)

def showCalories(calories1, calories2):
  print("The total calories you ate today: ", calories1 + calories2)

main()

# Q5: Write a program that uses any loop (while or for) that calculates the total of the following series of numbers:
#          1/30 + 2/29 + 3/28 ............. + 30/1

def total_sum():
  total = 0
  for n in range(1, 31):
    total += n / (31 - n)
  print(total)

total_sum()


# Q6: Write a function that computes the area of a triangle given its base and height.
# The formula for an area of a triangle is:
# AREA = 1/2 * BASE * HEIGHT

# For example, if the base was 5 and the height was 4, the area would be 10.
# triangle_area(5, 4)   # should print 10

def triangle_area(base, height):
  print(0.5 * base * height)

triangle_area(5, 4)
