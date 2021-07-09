from time import sleep
from turtle import Screen

from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("🕹 Pong ️🕹️")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')

while not scoreboard.is_game_over():
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with ceil and floor
    if not (-280 <= ball.ycor() <= 280):
        ball.bounce_wall()

    # Detect collision with paddles
    if not (-325 <= ball.xcor() <= 325) and left_paddle.distance(ball) < 50 or right_paddle.distance(ball) < 50:
        ball.bounce_paddle()

    # Detect collision with walls
    if not (-380 <= ball.xcor() <= 380):
        if ball.xcor() < -380:
            scoreboard.point('r')
        else:
            scoreboard.point('l')
        ball.reset_position()

scoreboard.game_over()

screen.exitonclick()
