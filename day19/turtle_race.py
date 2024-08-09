import turtle as t
import random

new=t.Screen()
new.bgpic("track.png")
new.setup(width=500,height=500)

colors=["purple","red","green","blue","black","cyan"]
pos=[-200,-133,-67,67,133,200]
all_tim=[]
for i in range(0,6):
    tim=t.Turtle()
    tim.shape("turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230,y=pos[i])
    all_tim.append(tim)

user_bet=new.textinput(title="make the bet: ",prompt="which turtle will win the race .state the color: ")
user_coin=int(new.textinput(title="coin",prompt="bet your coin: "))
is_on=False
if user_bet and user_coin:
    is_on=True
while is_on:
    for tim in all_tim:
        if tim.xcor()>=230:
            if tim.pencolor()==user_bet:
                print(f"you win. your coin got doubled!!{2*user_coin}")
                is_on=False
            else:
                print("you lose!!")
                is_on=False
            break
        dist=random.randint(0,10)
        tim.forward(dist)



new.exitonclick()
