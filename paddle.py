from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)
        self.speed("fastest")

    def move_up(self):
        new_yposition = self.ycor() + 20
        self.goto(self.xcor(), new_yposition)

    def move_down(self):
        new_yposition = self.ycor() - 20
        self.goto(self.xcor(), new_yposition)
