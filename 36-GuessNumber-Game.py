# GuessNumber Game
import random as r
from replit import clear

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

attempts_object = {
    "1": 10, # easy
    "2": 7,  # medium    
    "3": 5   # hard    
}

def init():
    clear()
    print(logo)
    print("Welcome to GuessNumber Game!")
    print("You have to guess a number between 1 and 100")
    dificulty = input("Choose a dificulty: \n1 - Easy\n2 - Medium\n3 - Hard\n")
    number = r.randint(1, 100)
    attempts = attempts_object[dificulty]
    print(f"You have {attempts} attempts")
    while attempts  > 0:
        guess = int(input("Guess a number: "))
        if guess == number:
            print("You win!")
            break
        elif guess > number:
            print("Too high")
        else:
            print("Too low")
            
        attempts -= 1
        print(f"You have {attempts} attempts left")
    
    option = input("Do you want to play again? (y/n): ")
    if option == "y":
        init()
    else:
        print("Good bye!")

init()


