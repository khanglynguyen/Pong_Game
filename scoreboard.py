from turtle import Turtle
FONT = ('Ariel', 32, 'bold')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(0,240)
        self.pendown()
        self.update()
    def l_update(self):
        self.l_score += 1
    def r_update(self):
        self.r_score += 1
    def update(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", False, align = "center", font= FONT)