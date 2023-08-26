# Blackjack Game
from replit import clear
from time import sleep
import random as r

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

setOfCards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

# Intialize the game
def init():
  clear()
  print(logo)
  option = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if option == "y":
    return True
  elif option == "n":
    return False
  else:
    print("Invalid input")
    sleep(2)
    return init()

#Game helpers Functions
def getCards(n):
  cards = list(range(n))
  for i in range(n):
    cards[i] = r.choice(setOfCards)
  return cards

def getScore(cards):
  for card in cards:
    if card ==  "J" or card == "Q" or card == "K":
      cards[cards.index(card)] = 10
    elif card == "A":
      cards[cards.index(card)] = 11
  print(cards) 
  return sum(cards)

def checkWinner(userScore, computerScore):
  print(f"Your final score is: {userScore}")
  print(f"Computer's final score is: {computerScore}")
  if userScore > 21:
    print("You went over. You Lose")
  elif computerScore > 21:
    print("Opponent went over. You Win")
  elif userScore == computerScore:
    print("Draw")
  elif userScore > computerScore:
    print("You Win")
  else:
    print("You Lose")
# End of Game helpers Functions

def game():
  userCards = [] # 2 cards + 1 card
  computerCards = [] # 2 cards + 1 card
  
  
  # Get the first 2 cards for the user
  userCards = getCards(2)
  # Get the first 2 cards for the computer
  computerCards = getCards(2)
  
  # Print the user cards and score
  print(f"Your cards: {userCards}")
  print(f"Computer's first card: {computerCards[0]}")
  
  option = input("Type 'y' to get another card, type 'n' to pass: ")
  if option == "y":
    userCards.append(getCards(1)[0])
    computerCards.append(getCards(1)[0])
    checkWinner(getScore(userCards), getScore(computerCards))
  elif option == "n":
    checkWinner(getScore(userCards), getScore(computerCards))
    
  sleep(10)

while init():
  game()