from turtle import Screen, Turtle
from paddle import Paddle

# Create the game Screen
screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
# Turn animation off
screen.tracer(0)

# Create the paddle
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# Listen to keyboard
screen.listen()

# Move Right Paddle
screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)

# Move Left Paddle
screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)

game_is_on = True
while game_is_on:
    # Refresh the screen to show elements after turning animation off
    screen.update()


# Keep the window open
screen.exitonclick()
