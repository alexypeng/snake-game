from turtle import Turtle
import random


class Apple(Turtle):
    """Creates the apple in the snake game. Inherits from the Turtle class."""
    def __init__(self):
        """Initializes the apple and defines the variables."""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.generate_position()

    def generate_position(self):
        """Generates a random position for the apple."""
        random_x = random.randint(-14, 14) * 20
        random_y = random.randint(-14, 14) * 20
        self.goto(random_x, random_y)
