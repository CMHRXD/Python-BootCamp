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
      cards.remove(card)
      if sum(cards) >= 10:
        cards.append(1)
      else:
        cards.append(11)
        
  return sum(cards)

def checkWinner(userScore, computerScore):
  print(f"Your final score is: {userScore}")
  print(f"Computer's final score is: {computerScore}")

  if userScore == computerScore:
    print("Draw")
  elif userScore > computerScore:
    print("You Win")
  else:
    print("You Lose")

def computerTurn(cards, userScore, round):
  computerScore = getScore(cards)
  if computerScore > 16 and round == 1:
    return computerScore
  else:  
    if userScore > computerScore and computerScore < 21:
      cards.append(r.choice(setOfCards))
      round += 1
      return computerTurn(cards, userScore,round)
    else:
      return computerScore

def userTurn(cards):
  userScore = getScore(cards)
  if userScore > 21:
    return userScore 
  option = input("Type 'h' to get another card, type 's' to pass: ")
  if option == "h":
    cards.append(r.choice(setOfCards))
    print(f"Your cards: {cards} - current score: {getScore(cards)}")
    return userTurn(cards)
  elif option == "s":
    return userScore
  else:
    print("Invalid input")
    sleep(2)
    return userTurn(cards)
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
  
  if getScore(userCards) == 21 and getScore(computerCards) == 21:
    print("Tie!")
    return
  
  if getScore(userCards) == 21:
    print("Blackjack! You Win")
    return
  
  if getScore(computerCards) == 21:
    print("Blackjack! You Lose")
    return
  
  userScore = userTurn(userCards)
  if userScore > 21:
    print("You went over. You Lose")
    return
  computerScore = computerTurn(computerCards, getScore(userCards), round=1)
  if computerScore > 21:
    print("Computer went over. You Win")
    return
  checkWinner(userScore, computerScore)

  sleep(15)

while init():
  game()