# Exercise: The Secret Auction
from replit import clear

# bid logo
logo = """
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
"""
print(logo)
print("Welcome to the Secret Auction")


bids = {}

def find_highest_bidder(bidding_record):
  # max returns the highest value in a dictionary and zip returns a tuple of the highest value and the key associated with it
  result = max(zip(bidding_record.values(), bidding_record.keys())) 
  highest_bid = result[0]
  winner = result[1]
  print(f"The winner is {winner} with a bid of ${highest_bid}")
  
while True:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  bids[name] = bid
  
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if should_continue == "no":
    find_highest_bidder(bids)
    break
  else:
    clear()