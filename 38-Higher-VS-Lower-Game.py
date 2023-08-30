from helpers.Higher_Vs_Lower_data import data, logo, vs
from random import choices
from replit import clear

global score
score = 0
def compare (optionA,optionB):
  if optionA[1] > optionB[1]:
    print("Congratulation you won")
    score+=1
    return "w"
  else:
    print(f"Sorry thats wrong. Final Score: {score}")
    return "lose"

def getData():
  result = choices(data)[0]
  return [f"{result['name']} a {result['description']} from {result['country']}", result['follower_count']]

def init ():
  clear()
  print(logo)
  # Compare A
  optionA = getData()
  print(optionA[0])
  
  #Print VS logo
  print(vs)
  
  #Compare b
  optionB = getData()
  print(optionB[0])
  
  choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  if choice == "a":
    value = compare(optionA,optionB)
  else:
    value = compare(optionB,optionA)
  
  option = input("You wana keep playing? Type 'y' or 'n': ").lower()
  if option == "y":
    if value != "w":
       score = 0
       
    return True
  else:
    print(f"Final Score: {score}")
    return False
  
while init():
  pass