
from turtle import *

# Turtule Basics
# ------------------------------

# Create a turtle
t = Turtle()

# Move the turtle forward by 100 units
t.forward(100)

# Move the turtle backward by 100 units
t.backward(100)

# Rotate the turtle left by 90 degrees
t.left(90)

# Rotate the turtle right by 90 degrees
t.right(90)

# Move the turtle to the origin
t.home()

# Clear the screen
t.clear()

# Hide the turtle
t.hideturtle()

# Show the turtle
t.showturtle()

# Set the turtle's color to red
t.color('red')

# Draw a circle with radius 50
t.circle(50)

# Draw a circle with radius 50 and fill it with red
t.begin_fill()
t.color('black', 'red')
t.circle(50)

# End the fill
t.end_fill()

# Dont close the window
done()

