
from turtle import Turtle as T, done as D
figure = T()
  
color = ["red","black", "blue", "green", "yellow","pink", "orange", "magenta", "gray"]
for i in range(3,11):
  figure.color(color[i-3])
  for f in range(i):
    figure.right(360/i)
    figure.forward(100)
    
D()