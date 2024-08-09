import turtle as  t
tim=t.Turtle()
new=t.Screen()

def move_forward():
    tim.forward(100)

def move_backward():
    tim.backward(100)

def turn_right():
    new=tim.heading()+10
    tim.setheading(new)
def turn_left():
    new=tim.heading()-10
    tim.setheading(new)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


new.listen()
new.onkey(move_backward,"w")
new.onkey(move_forward,"a")
new.onkey(turn_left,"s")
new.onkey(turn_right,"d")
new.onkey(clear,"c")

new.exitonclick()
