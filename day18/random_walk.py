import turtle as t
import random
timmy=t.Turtle()
timmy.speed("fast")
color=["green1","LightSeaGreen","DodgerBlue","DeepSkyBlue2","Firebrick1","red","salmon","dark violet","cornflower blue","deep sky blue","dark cyan"]
directions=[0,90,180,270]

for _ in range(200):
    timmy.pensize("7")
    timmy.color(random.choice(color))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

t.exitonclick()
