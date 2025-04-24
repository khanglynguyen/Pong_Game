from turtle import Turtle
from food import Food

STARTING_POSITION = [(0, 0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.square = []
        self.create_snake()
        self.head = self.square[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_square(position)
    def add_square(self,position):
        new_square = Turtle("turtle")
        new_square.color("green","green")
        new_square.penup()
        new_square.goto(position)
        self.square.append(new_square)

    def extend(self):
        last_position = len(self.square) - 1
        postion = self.square[last_position].pos()
        self.add_square(postion)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    
    def move(self):
        for square_num in range(len(self.square)-1, 0, -1):
            new_x = self.square[square_num -1].xcor()
            new_y = self.square[square_num -1].ycor()
            self.square[square_num].goto(new_x, new_y)
            # if new_x >= 300:
            #     self.square[square_num -1].teleport(-300,new_y)
            # elif new_x <= -300:
            #     self.square[square_num -1].teleport(300,new_y)

            # if new_y >= 300:
            #     self.square[square_num -1].teleport(new_x,-300)
            # elif new_y <= -300:
            #     self.square[square_num -1].teleport(new_x,300)
            self.square[square_num -1].fd(MOVE_DISTANCE)
    # def add_square(self):
    #     newsquare_xcor = self.square[len(self.square) -1].xcor()
    #     newsquare_ycor = self.square[len(self.square) -1].ycor()
    #     newsquare = Turtle("turtle")
    #     newsquare.color("green","green")
    #     newsquare.penup()
    #     newsquare.goto(newsquare_xcor,newsquare_ycor)           
    #     self.square.append(newsquare)
    # def if_hit(self,food_object):    
    #     square0_xcor = int(self.head.xcor())
    #     square0_ycor = int(self.head.ycor())
    #     foodobject_xcor = int(food_object.xcor)
    #     foodobject_ycor = int(food_object.ycor)
    #     if square0_xcor in range (foodobject_xcor -2, foodobject_xcor +2)  and square0_ycor in range(foodobject_ycor-2, foodobject_ycor+2):
    #         food_object.square.hideturtle()
    #         newsquare_xcor = self.square[len(self.square) -1].xcor()
    #         newsquare_ycor = self.square[len(self.square) -1].ycor()
    #         newsquare = Turtle("turtle")
    #         newsquare.color("green","green")
    #         newsquare.penup()
    #         newsquare.goto(newsquare_xcor,newsquare_ycor)
    #         # newsquare.backward(20)           
    #         self.square.append(newsquare)
    #         return True
