#Dictionaries in Python
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
#Dictionaries are written with curly brackets, and have keys and values:
#Example
#Create and print a dictionary:
#thisdict = {
#  "brand": "Ford",
#  "model": "Mustang",
#  "year": 1964
#}
#print(thisdict)
#Dictionary Items
#Dictionary items are ordered, changeable, and does not allow duplicates.
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
#Example
#Print the "brand" value of the dictionary:
#thisdict = {
#  "brand": "Ford",
#  "model": "Mustang",
#  "year": 1964
#}
#print(thisdict["brand"])
#Ordered or Unordered?
#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
#When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
#Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.
#Changeable
#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
#Duplicates Not Allowed
#Dictionaries cannot have two items with the same key:
#Example
#Duplicate values will overwrite existing values:
#thisdict = {
#  "brand": "Ford",
#  "model": "Mustang",
#  "year": 1964,
#  "year": 2020
#}
#print(thisdict)

thisdict = {
 "brand": "Ford",
 "model": "Mustang",
 "year": 1964
}
x = thisdict.get("model") # get the value of the "model" key
print(x)

keys = thisdict.keys() # get the keys of the dictionary

print(len(thisdict))  # get the length of the dictionary (number of key-value pairs) -> 3


for key, value in thisdict.items():
  print(key, value) # print all key names in the dictionary, one by one