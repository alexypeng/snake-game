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
        self.high_score = 0
        self.write_score()


    def write_score(self):
        """Write the score to the screen."""
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase the score by 1."""
        self.score += 1
        self.write_score()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.write_score()
