from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 70, "bold"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 70, "bold"))

    def add_point(self, player):
        if player == "left":
            self.left_score += 1
        else:
            self.right_score += 1
        self.update_score()
