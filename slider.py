from turtle import Turtle
MOVE_DISTANCE = 20

class Slider(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid = 5, stretch_len= 1)
        self.speed("fastest")
        self.goto(position)        

    def go_up(self):
        self.goto(self.xcor(),self.ycor() + MOVE_DISTANCE)
    
    def go_down(self):
        self.goto(self.xcor(),self.ycor() - MOVE_DISTANCE)

