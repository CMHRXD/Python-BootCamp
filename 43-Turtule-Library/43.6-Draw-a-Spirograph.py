
from turtle import Turtle as T, done, colormode
from random import randint
def rgbColor ():
  r = randint(0,255)
  g = randint(0,255)
  b = randint(0,255)
  
  return tuple((r,g,b))

figure = T()
figure.speed(0)
colormode(255)

for i in range(0,101):
  figure.left(3.6)
  figure.circle(90)
  figure.color(rgbColor())
  
done()
