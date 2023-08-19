# Cesar Cypher Exercice
# 
# Given a string, replace every letter with its position in the alphabet. If anything in the text isn't a letter, ignore it and don't return it.
#
# Example:
# Input: abcd
# Output: bcde
#
alphabet_array = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt_decrypt(text, shift, direction):
  new_word = ""
  for letter in text:
    index = alphabet_array.index(letter)
    new_word+= alphabet_array[ index-shift if direction == "decode" else index+shift]
    
  return new_word

if(direction == "encode"):
  result = encrypt_decrypt(text, shift, direction)
  print(f"The encrypted word is {result}")
  
elif(direction == "decode"):
  result = encrypt_decrypt(text, shift, direction)
  print(f"The decrypted word is {result}")
else:
  print("Invalid input")