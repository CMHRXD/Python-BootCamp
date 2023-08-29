# Debuggin exercise:

import pdb
import math as Math

def add(num1, num2):
    pdb.set_trace()
    try:
      return Math.Number(num1) + Math.Number(num2)
    except:
      print("Invalid input")
      return 0
  
add(4, '5')

#Solution:
 #use try and except to catch the error
 #try to convert the string to int
 #if it fails, return 0