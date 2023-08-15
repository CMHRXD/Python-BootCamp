import random as r

"""
  Rock Paper Scissors
  
  Rules:
  Rock beats Scissors
  Scissors beats Paper
  Paper beats Rock

"""

print("Welcome to Rock Paper Scissors!")

options = ["Rock", "Paper", "Scissors"]

computer_choice = r.choice(options)
user_choice = input("Enter your choice: ")

print("Computer's choice: ", computer_choice)
print("User's choice: ", user_choice)

if computer_choice == user_choice:
    print("It's a tie!")
elif computer_choice == "Rock" and user_choice == "Scissors":
    print("Computer wins!")
    
elif computer_choice == "Scissors" and user_choice == "Paper":
    print("Computer wins!")
    
elif computer_choice == "Paper" and user_choice == "Rock":
    print("Computer wins!")
    
else:
    print("User wins!")
    