from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)

    def move(self):
        new_xposition = self.xcor() + 10
        new_yposition = self.ycor() + 10
        self.goto(new_xposition, new_yposition)

