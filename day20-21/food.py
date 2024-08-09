from turtle import Turtle
import random
shapes=["circle","square","triangle"]
colors=["red","green","blue","violet"]
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(random.choice(shapes))
        self.penup()
        self.color(random.choice(colors))
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        random_x=random.randint(-280,280)
        random_y=random.randint(-280,260)
        self.goto(random_x,random_y)

    def refresh(self):
            random_x=random.randint(-280,280)
            random_y=random.randint(-280,280)
            self.goto(random_x,random_y)
