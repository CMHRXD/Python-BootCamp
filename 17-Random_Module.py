# Random Modules
# Random module is used to generate random numbers in Python.
#
# There are 4 types of Random Modules in Python:
#
# 1. random()
# 2. randint()
# 3. randrange()
# 4. choice()
#
# random()
# random() function is used to generate a random floating point number between 0 and 1.
#
# Syntax:
# random()
#
# Example 1:
# random()
import random
print(random.random()) # 0.4288890546751146
print(random.random() * 5) # 0 to 5 in decimal
print(random.random() * 10) # 0 to 10 in decimal

# Example 2:
# randint()
# randint() function is used to generate a random integer between the given range.
#
# Syntax:
# randint(start, end)
#
# Example 1:
# randint(start, end)
print(random.randint(1, 10)) # 7

# RandRange()
# randrange() function is used to generate a random integer between the given range.
#
# Syntax:
# randrange(start, end, step)
#
# Example 1:
# randrange(start, end, step)
print(random.randrange(1, 10, 2)) # 5

# Choice()
# choice() function is used to generate a random element from the given sequence.
#
# Syntax:
# choice(sequence)
#
# Example 1:
# choice(sequence)
print(random.choice([1, 2, 3, 4, 5])) # 3
print(random.choice("Hello World")) # l

