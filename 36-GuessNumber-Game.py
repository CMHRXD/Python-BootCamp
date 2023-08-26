# GuessNumber Game
import random as r

attempts_object = {
    "1": 10, # easy
    "2": 7,  # medium    
    "3": 5   # hard    
}

def init():
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

init()


