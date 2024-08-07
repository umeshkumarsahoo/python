import turtle as t
import random
timmy=t.Turtle()
timmy.speed("fastest")


colors = [
    "green1", "LightSeaGreen", "DodgerBlue", "DeepSkyBlue2", "Firebrick1", "red",
    "salmon", "dark violet", "cornflower blue", "deep sky blue", "dark cyan",
    "medium purple", "yellow", "orange", "gold", "orchid", "medium orchid",
    "medium slate blue", "spring green", "light coral", "indian red", "cyan"
]

def draw(size):
    for _ in range(round(360/size)):
        timmy.color(random.choice(colors))
        timmy.circle(80)
        timmy.setheading(timmy.heading()+size)

draw(5)




screen=t.Screen
t.exitonclick()
