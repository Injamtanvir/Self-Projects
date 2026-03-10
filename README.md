# Pong Game (Python Turtle)

This project is a simple 2-player Pong game built with Python's `turtle` module.

## 1. What You Will Build

- A black game screen (800x600)
- Two paddles (left and right)
- One moving ball
- Ball bounce on top/bottom walls
- Ball bounce on paddles
- Scoreboard for both players
- Ball reset when a player misses

## 2. Prerequisites

- Python 3 installed
- No extra package required (`turtle` and `time` are built-in)

Run the game:

```bash
uv run python main.py
```

## 3. Project Files

- `main.py` --> game loop + object creation + collision logic
- `paddle.py` --> `Paddle` class (move up/down)
- `ball.py` --> `Ball` class (move + bounce + speed)
- `scoreboard.py` --> `Scoreboard` class (left/right points)
- `NOTES.TXT` --> raw notes used to build this project

## 4. Controls

- Right paddle: `Up` and `Down` arrow keys
- Left paddle: `W` and `S`

## 5. Build It From Scratch (Step by Step)

## Step 1: Create `main.py` and the screen

```python
from turtle import Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

screen.exitonclick()
```

Why `tracer(0)`?
It turns off auto-refresh so we can control updates manually with `screen.update()` inside the game loop.

## Step 2: Create `paddle.py`

```python
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
```

A turtle square is 20x20 by default.
`stretch_wid=5` makes paddle height `5 x 20 = 100`.

## Step 3: Use paddles in `main.py`

```python
from paddle import Paddle

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
```

## Step 4: Create `ball.py`

```python
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
```

Speed logic:
- Start delay: `0.1` seconds per frame
- On paddle hit: `move_speed *= 0.9` (game gets faster)
- On miss/reset: speed goes back to `0.1`

## Step 5: Create `scoreboard.py`

```python
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
```

## Step 6: Final game loop in `main.py`

```python
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Top/bottom wall bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Paddle bounce
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or \
       (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Right player missed
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Left player missed
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
```

## 6. How the Game Logic Works

Each loop does this:

1. Wait `ball.move_speed` seconds
2. Redraw screen
3. Move ball
4. Check wall collision (`y` limits)
5. Check paddle collision
6. Check if ball passed left/right edge
7. Update score and reset ball when needed
