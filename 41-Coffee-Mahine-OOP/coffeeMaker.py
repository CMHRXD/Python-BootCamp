
# Coffee Maker Class - Blueprint for creating new coffee makers
class CoffeeMaker:
  def __init__(self, resources):
    self.resources = resources
    
  def report(self):
    print("----- Report -----")
    print("Water: ", self.resources["water"])
    print("Milk: ", self.resources["milk"])
    print("Coffee: ", self.resources["coffee"])
    
  def isResourceSufficient(self, drink):
    for key in drink.ingredients:
      if self.resources[key] < drink.ingredients[key]:
        print(f"Sorry there is not enough {key}.")
        return False
    return True

  def makeCoffee(self, order):
    for key in order.ingredients:
      self.resources[key] -= order.ingredients[key]
    print("Here is your coffee. Enjoy!")
    
  