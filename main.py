from turtle import Screen
from snake import Snake
from apple import Apple
from scoreboard import Scoreboard
import time

game_is_on = True

s = Screen()
s.setup(width=600, height=600)

s.bgcolor("black")
s.title(titlestring="Snake Game")
s.tracer(0)

snake = Snake()
apple = Apple()
scoreboard = Scoreboard()

s.update()

s.listen()
s.onkey(key="Up", fun=snake.up)
s.onkey(key="Down", fun=snake.down)
s.onkey(key="Left", fun=snake.left)
s.onkey(key="Right", fun=snake.right)

while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(apple) < 15:
        apple.generate_position()
        scoreboard.increase_score()
        snake.extend()

    if snake.check_collision():
        game_is_on = False

scoreboard.game_over()

s.exitonclick()
