from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.refresh()
        self.color("blue","blue")
        self.showturtle()
    def refresh(self):
        self.goto(random.randrange(-260,261,20), random.randrange(-260,261,20))



