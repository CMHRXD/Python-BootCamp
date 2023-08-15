#LISTS IN PYTHON

# Lists are mutable, ordered, and allow duplicate elements
# Lists are defined with square brackets
# Lists can be created with the list() constructor

# Create a list
my_list = ["banana", "cherry", "apple"]
print(my_list)

# Create a list using the list() constructor
my_list2 = list()
print(my_list2)

# Create a list with mixed data types
my_list3 = [5, True, "apple", "apple"]
print(my_list3)

# Get the length of a list
item_count = len(my_list3)
print(item_count)

# Access an item in a list by index
item = my_list3[0]
print(item)

# Access an item in a list by index
item = my_list3[-1]

# Change the value of an item in a list
my_list3[0] = "pear"

# Loop through a list
for item in my_list3:
    print(item)

# Check if an item is in a list
if "banana" in my_list3:
    print("yes")
else:
    print("no")
    
# Add an item to the end of a list
my_list3.append("orange")
print(my_list3)

# Add an item at a specified index
# my_list3.insert(index, item)
my_list3.insert(1, "blueberry")
print(my_list3)

# Remove an item from a list
item = my_list3.pop()
print(item)

# Remove an item from a list at a specified index
item = my_list3.pop(0)
print(item)

# Remove an item from a list by value
my_list3.remove("apple")
print(my_list3)

# Remove all items from a list
my_list3.clear()
print(my_list3)

# Reverse the order of items in a list
my_list3 = ["banana", "cherry", "apple"]
my_list3.reverse() # reverse also mutates the list

print(my_list3)

# Sort items in a list in ascending order
my_list3.sort()
print(my_list3)

# Sort items in a list in descending order
my_list3.sort(reverse=True)
print(my_list3)

# Create a copy of a list
my_list4 = my_list3.copy()

# Create a copy of a list using the list() constructor
my_list5 = list(my_list3)

# Join two lists
my_list6 = my_list3 + my_list4

# Slicing a list
# my_list3[start:end:step]
my_list7 = my_list3[1:3]

# Return the index of the first item that matches the search criteria
# my_list3.index(item, start, end)
index = my_list3.index("cherry", 0, 3)
index = my_list3.index("cherry")

# Count the number of times an item appears in a list
count = my_list3.count("apple")

# Convert a list to a string ["1", "2", "3"] -> "1, 2, 3"
my_string = ", ".join(my_list3) # "banana, cherry, apple"
my_string = " - ".join(my_list3) # "banana - cherry - apple"

# Convert a string to a list "1, 2, 3" -> ["1", "2", "3"]
my_list8 = my_string.split(", ") # ["banana", "cherry", "apple"]
my_list8 = my_string.split(" - ") # ["banana", "cherry", "apple"]

# List comprehension

# Create a list of squares from 1 to 10
# Syntax [expression for item in iterable]
my_list9 = [i * i for i in range(1, 11)]
print(my_list9)

# Create a list of numbers from 1 to 10 that are divisible by 2
# Syntax [expression for item in iterable if condition]
my_list10 = [i for i in range(1, 11) if i % 2 == 0]
    
        
print(my_list10)





