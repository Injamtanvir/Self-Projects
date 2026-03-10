from turtle import Screen, Turtle   # importing a screen from the turtle module
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black") # background color
screen.setup(width=800, height=600) # screen size
screen.title("Pong")
screen.tracer(0) # turn off animation

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up") # for left user
screen.onkey(r_paddle.go_down, "Down") # for left user
screen.onkey(l_paddle.go_up, "w") # for right user
screen.onkey(l_paddle.go_down, "s") # for right user

# If you have turned off the animation you need to update the screen manually and refreshed it.
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update() # update the screen
    ball.move()     

    #Detect collision with wall (top)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        # If the ball has gone far enough to the right or left and is within 50 pixels of the paddle, it is considered a collision.
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick() # exit on click