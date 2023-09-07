from turtle import Turtle as T, done, colormode
from random import choice, randint

random_walk = T()
random_walk.pensize(30)
colormode(255)

def rgbColor ():
  r = randint(0,255)
  g = randint(0,255)
  b = randint(0,255)
  
  return tuple((r,g,b))

def movement(number, direction):
    if direction == "right":
        random_walk.left(number)
        random_walk.forward(100)
    else:
        random_walk.left(number)
        random_walk.forward(100)
    random_walk.color(rgbColor())
    random_walk.speed(10)


while True:
    number = choice([0,90,180,270])
    direction = choice(["right", "left"])
    movement(number, direction)
