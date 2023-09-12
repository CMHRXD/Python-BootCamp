from turtle import Turtle, Screen
from random import randint

tim = Turtle(shape="turtle")
rob = Turtle(shape="turtle")
rolf = Turtle(shape="turtle")
tirion = Turtle(shape="turtle")
jimmy = Turtle(shape="turtle")

window = Screen()
window.setup(700, 400)

def goToStartingPosition(turtle, y):
    turtle.penup()
    turtle.goto(x=-290, y=y)
    turtle.pendown()

def move (turtle):
    turtle.forward(randint(1, 10))
    if turtle.xcor() > 300:
        print(f"The winner is {turtle.pencolor()}")
        return True
    else:
        return False

def drowFinishLine():
  line = Turtle()
  line.penup()
  line.color("red")
  line.goto(x=300, y=200)
  line.pendown()
  line.goto(x=300, y=-200)
  line.hideturtle()


# Define colors
rolf.color("red")
rob.color("blue")
tim.color("green")
tirion.color("yellow")
jimmy.color("orange")

# Define starting positions
goToStartingPosition(rolf, 100)
goToStartingPosition(rob, 50)
goToStartingPosition(tim, 0)
goToStartingPosition(tirion, -50)
goToStartingPosition(jimmy, -100)

drowFinishLine()

# Start Race
while True:
  if move(rolf) or move(rob) or move(tim) or move(tirion) or move(jimmy):
    break

window.exitonclick()