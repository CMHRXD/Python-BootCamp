# Menu Class - Blueprint for creating new menus

class Menu:
  def __init__(self):
    self.menu = []
    
  def addMenuItem(self, item):
    self.menu.append(item)
    
  def printMenu(self):
    menu = ""
    for item in self.menu:
      menu+=(f"\n{item.name[0]}: ${item.cost[0]}")
    return menu
  
  def findMenuItem(self, name):
    for item in self.menu:
      if item.name[0] == name:
        return item
    return None
  
  def removeMenuItem(self, name):
    item = self.findMenuItem(name)
    if item:
      self.menu.remove(item)
      print(f"{name} removed from menu.")
    else:
      print(f"{name} not found in menu.")
  