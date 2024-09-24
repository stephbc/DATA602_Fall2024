# Stephanie Chiang
# Data 607 Fall 2024 Assignment 5

# Q1: Create a class called BankAccount, etc...

class BankAccount:
  def __init__(self, bankname, firstname, lastname, balance = 0):
    self.bankname = bankname
    self.firstname = firstname
    self.lastname = lastname
    self.balance = balance

  def deposit(self, money):
    if money > 0:
      self.balance += money
      print(f"Deposit of {money} accepted. Your balance is now {self.balance}.")
    else:
      print("Invalid entry. Please try again.")

  def withdrawal(self, money):
    if money <= self.balance and money > 0:
      self.balance -= money
      print(f"{money} withdrawn. Your balance is now {self.balance}.")
    elif money > self.balance:
      print(f"Insufficient funds in {self.bankname} account. Your balance is {self.balance}.")
    else:
      print("Invalid entry. Please try again.")

  def __str__(self):
    return f"Bank Name: {self.bankname}, Account Name: {self.firstname} {self.lastname}, Balance: ${self.balance}"

# TESTING

puckChase = BankAccount("Chase", "Puck", "Hoang")
puckChase.deposit(500)
# Deposit of 500 accepted. Your balance is now 500.
puckChase.withdrawal(200)
#200 withdrawn. Your balance is now 300.
puckChase.withdrawal(1000)
# Insufficient funds in Chase account. Your balance is 300.
puckChase.deposit(-123)
# Invalid entry. Please try again.
print(puckChase)
# Bank Name: Chase, Account Name: Puck Hoang, Balance: $300

puckCiti = BankAccount("Citi", "Puck", "Hoang", 50)
print(puckCiti)
# Citi, Account Name: Puck Hoang, Balance: $50
puckCiti.withdrawal(49)
# 49 withdrawn. Your balance is now 1.
puckCiti.deposit(500)
# Deposit of 500 accepted. Your balance is now 501.
print(puckCiti)
# Bank Name: Citi, Account Name: Puck Hoang, Balance: $501


# Q2: Create a class Box...

import math

class Box():
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def render(self):
    for _ in range(self.length):
      print("*" * self.width)

  def invert(self):
    self.length, self.width = self.width, self.length
    return self.render()

  def get_area(self):
    return self.length * self.width

  def get_perimeter(self):
    return 2 * (self.length + self.width)

  def double(self):
    self.length *= 2
    self.width *= 2
    return self.render()

  def __eq__(self, box2):
    return self.length == box2.length and self.width == box2.width

  def print_dim(self):
    print(f"The length is {self.length} and the width is {self.width}.")

  def get_dim(self):
    return (self.length, self.width)

  def combine(self, box2):
    self.length += box2.length
    self.width += box2.width
    return self.render()

  def get_hypot(self):
    return math.sqrt(self.length**2 + self.width**2)


# TESTING

box1 = Box(5, 10)
box2 = Box(3, 4)
box3 = Box(5, 10)

box1.print_dim()
# The length is 5 and the width is 10.
box2.print_dim()
# The length is 3 and the width is 4.
box3.print_dim()
# The length is 5 and the width is 10.
print(box1 == box2)
# False
print(box1 == box3)
# True

box1.render()
# **********
# **********
# **********
# **********
# **********

box1.combine(box3)
# ********************
# ********************
# ********************
# ********************
# ********************
# ********************
# ********************
# ********************
# ********************
# ********************

box2.render()
# ****
# ****
# ****

box2.double()
# ********
# ********
# ********
# ********
# ********
# ********

box1.combine(box2)
# ****************************
# ****************************
# ****************************
# ****************************
# ****************************
# ****************************
# ****************************
# ****************************
# ****************************
# ****************************
# ****************************
# ****************************
# ****************************
# ****************************
# ****************************
# ****************************

# EXTRA TESTING

# box2.render()
# box2.invert()
# print(box1.get_area())
# print(box3.get_perimeter())
# print(box1.get_dim())
# box3.print_dim()
# print(box2.get_hypot())
