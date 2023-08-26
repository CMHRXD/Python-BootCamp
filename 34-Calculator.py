# Calculator with Python
from replit import clear
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def calculate(n1, n2, operation, result):
  if operation == "+":
    result = (n1 + n2)
  elif operation == "-":
    result = (n1 - n2)
  elif operation == "*":
    result = (n1 * n2)
  elif operation == "/":
    result = (n1 / n2)
  else:
    print("Invalid operation")
  print(f"{n1} {operation} {n2} = {result}")
  return result
  
def init(result):
  print(logo)
  if result == 0:
    n1 = float(input("What's the first number?: "))
  else:
    n1 = result
  print("+\n-\n*\n/\n")
  operation = input("Pick an operation from the line above: ")
  n2 = float(input("What's the second number?: "))
  return calculate(n1, n2, operation, result)

counter = 0
while True:
  if counter == 0:
    result = init(0)
    counter += 1

  foward_operation = input(f"Type y to continue calculating with {result}, or type n to start a new calculation? ")
  if foward_operation == "y":
    result = init(result)
  elif foward_operation == "n":
    clear()
    break
  else:
    print("Invalid input")
    break
  