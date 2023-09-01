# Object Oriented Programming

# Class: Blueprint for creating new objects
# Object: Instance of a class


# Class: Human
# Objects: John, Mary, Jack
class Human:
    def __init__(self, name, age): # Constructor
        self.name = name # Attributes
        self.age = age # Attributess
    def speak(self):
        print(f"Hello, my name is {self.name}, and I am {self.age} years old.")
# Instantiate a class
john = Human("John", 36)
john.speak()


# Class: Car
# Objects: Honda, Toyota, BMW
# Attributes: color, model, year
# Private Attributes: _color, _model, _year
# Methods: drive, stop, park

class Car:
  def __init__(self):
    self.__color = "red"
    self.__model = "Honda"
    self.__year = 2020
    
  def drive(self):
    print("Driving...")
    
  def stop(self):
    print("Stopping...")
    
  def park(self):
    print("Parking...")
  
    
    
honda = Car()
honda.drive()
honda.stop()
honda.park()
print(honda.__color) # AttributeError: 'Car' object has no attribute '__color'