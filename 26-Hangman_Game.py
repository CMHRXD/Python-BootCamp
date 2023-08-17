"""
Hangman Game

Rules:
    1. The computer will think of a random word from the list.
    2. The player guesses one letter at a time.
    3. The player has 6 lives.
    4. The game ends when the player guesses the word or runs out of lives.
"""

import random as r

def word_fill(chosen_word, guess, unknown_word):
  index = chosen_word.index(guess)
  unknown_word[index] = guess
  return unknown_word

hangman_art = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]
hangman_art.reverse()
word_list = ["aardvark", "baboon", "camel", "cat", "dog", "elephant", "giraffe", "lion", "monkey", "mouse", "panda", "penguin", "rabbit", "snake", "tiger", "wolf", "zebra"]

chosen_word = r.choice(word_list) # random.choice() returns a random element from the non-empty sequence seq
word_length = len(chosen_word) # len() returns the number of items in an object
game_over = False # game_over is a boolean variable
lives = 7 # lives is an integer variable

unknown_word = list(word_length * "_") # unknown_word is a list variable

print("WELOCOME TO HANGMAN GAME\n")
print("You have 6 tries to guess the final word \n")
print(f"{' '.join(unknown_word)}\n")
print(chosen_word)

while not game_over:
  guess = input("Guess a letter: ").lower()
  if guess in chosen_word:
    repeated_letter = chosen_word.count(guess)
    if repeated_letter > 1: # case when the letter is repeated more than once in the word
      for i in range(repeated_letter):
        unknown_word = word_fill(chosen_word, guess, unknown_word)
        chosen_word = chosen_word.replace(guess, "_", 1)
    else:
        unknown_word = word_fill(chosen_word, guess, unknown_word)
  else:
    lives-=1
    print(f"You have {lives} lives left to guess the final word \n")
    print(hangman_art[lives])
    
  if lives == 0:
    game_over = True
    print("You lose!")
    
  if "_" not in unknown_word:
    game_over = True
    print("You win!")
    
  print(f"{' '.join(unknown_word)}\n")
  
    
    
    

