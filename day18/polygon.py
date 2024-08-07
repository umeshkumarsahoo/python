import turtle as t
import random
timmy=t.Turtle()

color=["green1","LightSeaGreen","DodgerBlue","DeepSkyBlue2","Firebrick1"]

def draw(no_sides):
    angle=360/no_sides
    for _ in range(no_sides):
        timmy.forward(70)
        timmy.right(angle)

for i in range(3,20):
    timmy.color(random.choice(color))
    draw(i)


t.exitonclick()
