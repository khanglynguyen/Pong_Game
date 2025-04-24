from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # self.setheading(random.randint(- self.startdegree, self.startdegree ))
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1
    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x,new_y)
    def bounce_cell(self):
        self.ymove *= -1
        self.move_speed *= 0.9
    def bounce_slider(self):
        self.xmove *= -1
        self.move_speed *= 0.9
    def restart(self):
        self.home()
        self.bounce_slider()