from turtle import Screen
from snake import Snake
import time

game_is_on = True

s = Screen()
s.setup(width=600, height=600)

s.bgcolor("black")
s.title(titlestring="Snake Game")
s.tracer(0)

snake = Snake()

s.update()

s.listen()

while game_is_on:
    s.update()
    time.sleep(0.1)

    s.onkey(key="Up", fun=snake.up)
    s.onkey(key="Down", fun=snake.down)
    s.onkey(key="Left", fun=snake.left)
    s.onkey(key="Right", fun=snake.right)

    snake.move()

    if snake.check_collision():
        game_is_on = False



s.exitonclick()
