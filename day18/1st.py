import turtle
from turtle import Turtle
timmy=Turtle()
timmy.color("green")
for i in range(0,10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

turtle.exitonclick()
