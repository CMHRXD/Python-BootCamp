from menu import Menu
from menuItem import MenuItem
from coffeeMaker import CoffeeMaker
from moneyMachine import MoneyMachine
from replit import clear
from time import sleep

# Initialize Menu
menu = Menu()
# Initialize Coffee Maker
coffeeMaker = CoffeeMaker({"water": 300, "milk": 200, "coffee": 100})
# Initialize MoneyMachine
moneyMachine = MoneyMachine()

# Menu Items
espresso = MenuItem("espresso", 1.50, {"water": 50, "coffee": 18})
latte = MenuItem("latte", 2.50, {"water": 200, "milk": 150, "coffee": 24})
cappuccino = MenuItem("cappuccino", 3.00, {"water": 250, "milk": 100, "coffee": 24})

# Add menu items to menu
menu.addMenuItem(espresso)
menu.addMenuItem(latte)
menu.addMenuItem(cappuccino)

# Start Coffee Machine
isOn = True
while isOn:
  clear()
  choice = input(f"What would you like? {menu.printMenu()}: \nChoice -> ").lower()
  if choice == "off":
    isOn = False
    moneyMachine.report()
  elif choice == "report":
    coffeeMaker.report()
    
  else:
    item = menu.findMenuItem(choice)
    if item:
      if coffeeMaker.isResourceSufficient(item):
        if moneyMachine.makePayment(item.cost[0]):
          coffeeMaker.makeCoffee(item)
      else:
        print(f"Sorry, {choice} is not available.")
    else:
      print(f"{choice} not found in menu.")
  sleep(4)
      
  