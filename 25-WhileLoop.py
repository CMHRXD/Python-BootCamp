# While Loop Syntax
# while condition:
#     # code
#     # code
#     # code
#

# while loop example
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
#

#While loop exercise 1
# iterate through a list and print out the items in the list one by one
fruits = ["Apple", "Peach", "Pear"]

while fruits:
    print(fruits.pop())

# While loop exercise 2
# Add all the even numbers from 1 to 100 to a list
data = []
i = 1
while i <= 100:
    if i%2 == 0:
        data.append(i)
    i += 1
print(data)