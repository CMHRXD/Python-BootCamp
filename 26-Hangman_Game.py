"""
Hangman Game

Rules:
    1. The computer will think of a random word from the list.
    2. The player guesses one letter at a time.
    3. The player has 6 lives.
    4. The game ends when the player guesses the word or runs out of lives.
"""

import random as r

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
word_list = ["aardvark", "baboon", "camel", "cat", "dog", "elephant", "giraffe", "lion", "monkey", "mouse", "panda", "penguin", "rabbit", "snake", "tiger", "wolf", "zebra"]


