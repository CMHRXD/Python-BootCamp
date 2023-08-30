MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
  "quarters": 0.25,
  "dimes": 0.10,
  "nickles": 0.05,
  "pennies": 0.01
}

profit = 0

def getCoins():
  quarters = (int(input("How many quarters? "))* coins["quarters"])
  dimes = (int(input("How many dimes? ")) * coins["dimes"])
  nickles = (int(input("How many nickles? ")) * coins["nickles"])
  pennies = (int(input("How many pennies? ")) * coins["pennies"])
  
  return quarters + dimes + nickles + pennies

def checkResources(ingredients):
  for key in ingredients:
    if resources[key] < ingredients[key]:
      print(f"Sorry there is not enough {key}.")
      return False
  return True

def handleBuy (ingredients, price):
  global resources
  global profit
  while True:
    userCoins = getCoins()
    if userCoins < price:
      print("Sorry that's not enough money. Money refunded.")
      continue
    elif userCoins >= price:
      break
  total = round(userCoins - price,3)
  
  resources["water"] -= ingredients["water"]
  resources["coffee"] -= ingredients["coffee"]
  if ingredients.get("milk"):
    resources["milk"] -= ingredients["milk"]
  
  profit += price
  return total

def handleReport():
  pass

def countinueBuying():
    repeat = input("Do you want to buy another coffee? (y/n): ").lower()
    if repeat == "y":
      init()
    else:
      print("Good Bye, your profit is: ", profit)

def init():
  option = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
  if option == "espresso" or option == "latte" or option == "cappuccino":
    
    if not checkResources(MENU[option]["ingredients"]):
      return countinueBuying()
    
    result = handleBuy(MENU[option]["ingredients"], MENU[option]["cost"])
    print("Here is your change: ", result)
    print(f"Here is your {option} ☕️. Enjoy!")
    
    countinueBuying()
    
  elif option == "report":
    print(f"Water: {resources['water']} \nMilk: {resources['milk']} \nCoffee: {resources['coffee']}")
    
  else:
    print("Invalid Option")
    
init()