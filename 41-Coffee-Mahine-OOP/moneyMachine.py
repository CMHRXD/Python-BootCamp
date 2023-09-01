
# Money Machine Class - Blueprint for creating new money machines
class MoneyMachine:
  
  COINS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
  }
  
  def __init__(self):
    self.money = 0.0
  
  def report(self):
    # The :.2f specifies that the value should be formatted as a float with two decimal places.
    print("----- Money Machine Report-----\n Your current balance is ${:.2f}".format(self.money))
  
  def makePayment(self, cost):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return self.isPaymentSufficient(cost, total)
    
  
  def isPaymentSufficient(self, cost, total):
    if total >= cost:
      change = total - cost
      print("Here is ${:.2f} in change.".format(change))
      self.money += cost
      return True
    else:
      print("Sorry that's not enough money. Money refunded.")
      return False