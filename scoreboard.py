from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "bold")


class Scoreboard(Turtle):
    """Class that creates a scoreboard. Inherits from the Turtle class."""
    def __init__(self):
        """Initialize the scoreboard and define the variables"""
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.write_score()

    def write_score(self):
        """Write the score to the screen."""
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase the score by 1."""
        self.score += 1
        self.write_score()

    def game_over(self):
        """Writes Game Over to the screen."""
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
