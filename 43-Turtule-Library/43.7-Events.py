# Events in Turtle
from turtle import Turtle, Screen

rolf = Turtle()

window = Screen()

def move_forwards():
  rolf.forward(10)
  
def move_backwards():
  rolf.backward(10)
  
def move_left():
  rolf.left(10)
  
def move_right():
  rolf.right(10)
  
  
window.listen()

window.onkey(key = "w", fun = move_forwards)
window.onkey(key = "s", fun = move_backwards)
window.onkey(key = "a", fun = move_left)
window.onkey(key = "d", fun = move_right)
window.onkey(key="c", fun=rolf.clear)

window.exitonclick()

