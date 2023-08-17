"""
Password Generator Exercise
"""
import random as r

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()_+"

print("Welcome to the PyPassword Generator!")

numbers_of_letters = int(input("How many letters would you like in your password?\n"))
numbers_of_symbols = int(input("How many symbols would you like?\n"))
numbers_of_numbers = int(input("How many numbers would you like?\n"))

password = []

for i in range(numbers_of_letters):
    password += r.choice(letters)
    
for i in range(numbers_of_symbols):
    password += r.choice(symbols)
    
for i in range(numbers_of_numbers):
    password += r.choice(numbers)
    
r.shuffle(password) # shuffle() mutate the list and shuffle the items in the list
print("".join(password)) # join() convert the list to a string
