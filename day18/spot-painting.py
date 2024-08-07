import colorgram
import random
import turtle as t
umu=t.Turtle()
new=t.Screen()
umu.hideturtle()
umu.speed("fastest")
new.screensize(2000, 1500)
rgb_colors=[ "green1", "LightSeaGreen", "DodgerBlue", "DeepSkyBlue2", "Firebrick1", "red",
    "salmon", "dark violet", "cornflower blue", "deep sky blue", "dark cyan",
    "medium purple", "yellow", "orange", "gold", "orchid", "medium orchid",
    "medium slate blue", "spring green", "light coral", "indian red", "cyan"]
count=0

def head(count):
    if count%2==0:
        umu.backward(50)
        umu.setheading(90)
        umu.forward(50)
        umu.setheading(180)
    else:
        umu.backward(50)
        umu.setheading(90)
        umu.forward(50)
        umu.setheading(0)
# setting the turtle position
umu.penup()
umu.setheading(220)
umu.forward(300)
umu.setheading(0)
#turtle print
def pri():
    for _ in range(10):
        umu.pendown()
        umu.dot(20,random.choice(rgb_colors))
        umu.penup()
        umu.forward(50)


for i in range(10):
    pri()
    head(i)














new.exitonclick()
